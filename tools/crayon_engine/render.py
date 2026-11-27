"""Renderer: cairo frames -> ffmpeg (H.264 High, yuv420p, 30 fps) + AAC audio.

Frames are rendered in parallel chunks (fork workers), each piped as raw BGRA into its own
ffmpeg encoder, then concatenated losslessly and muxed with the final audio mix.
"""
from __future__ import annotations

import math
import multiprocessing as mp
import os
import subprocess

import cairo

from .core import FPS, H, W, Frame

_TL = None  # timeline for forked workers


def draw_frame(tl, n: int, surface=None):
    T = n / FPS
    shot = tl.at(T)
    t = T - shot.start
    if surface is None:
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    ctx = cairo.Context(surface)
    ctx.set_antialias(cairo.ANTIALIAS_GOOD)
    ctx.set_source_rgb(0, 0, 0)
    ctx.paint()
    cam = shot.camera()
    z, fx, fy = cam.at(t, shot.dur)
    f = Frame(ctx=ctx, t=t, T=T, dur=shot.dur, zoom=z, shot_id=shot.id)
    sx, sy = shot.meta.get("_shake", lambda t: (0, 0))(t)
    ctx.translate(W / 2 + sx, H / 2 + sy)
    ctx.scale(z, z)
    ctx.translate(-fx, -fy)
    shot.draw(f)
    # screen-space overlays (not affected by camera): e.g. time cards
    if "overlay" in shot.meta:
        ctx.identity_matrix()
        f.zoom = 1.0
        shot.meta["overlay"](f)
    surface.flush()
    return surface


def still(tl, T: float, path: str):
    s = draw_frame(tl, int(round(T * FPS)))
    s.write_to_png(path)
    return path


def _encode_chunk(args):
    a, b, out = args
    tl = _TL
    p = subprocess.Popen(
        ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra",
         "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
         "-b:v", "14M", "-maxrate", "20M", "-bufsize", "28M", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-g", "60", "-bf", "2", "-x264-params", "keyint=60:min-keyint=30", out],
        stdin=subprocess.PIPE)
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    for n in range(a, b):
        draw_frame(tl, n, surf)
        p.stdin.write(bytes(surf.get_data()))
    p.stdin.close()
    p.wait()
    return out


def render(tl, out_mp4: str, audio: str | None, workdir: str, workers: int | None = None):
    global _TL
    _TL = tl
    os.makedirs(workdir, exist_ok=True)
    N = int(math.ceil(tl.total * FPS))
    workers = workers or max(1, (os.cpu_count() or 2))
    step = int(math.ceil(N / workers))
    jobs = [(i, min(N, i + step), os.path.join(workdir, f"chunk_{k:02d}.mp4"))
            for k, i in enumerate(range(0, N, step))]
    ctxm = mp.get_context("fork")
    with ctxm.Pool(len(jobs)) as pool:
        outs = pool.map(_encode_chunk, jobs)
    lst = os.path.join(workdir, "chunks.txt")
    with open(lst, "w") as fh:
        for o in outs:
            fh.write(f"file '{os.path.abspath(o)}'\n")
    video = os.path.join(workdir, "video.mp4")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", video], check=True)
    if audio:
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", video, "-i", audio,
                        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "320k",
                        "-ar", "48000", "-ac", "2", "-movflags", "+faststart", "-shortest", out_mp4], check=True)
    else:
        os.replace(video, out_mp4)
    for o in outs:
        os.remove(o)
    return out_mp4
