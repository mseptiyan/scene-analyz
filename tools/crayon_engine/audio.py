"""Procedural SFX (no licensed samples) + final mix at -14 LUFS / TP <= -1 dBTP.

SFX are synthesised from sines and filtered noise, so there is nothing to license. They sit
well below the VO (VO stays dominant; QC: "VO clear above music/SFX").
"""
from __future__ import annotations

import os

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt

SR = 48000


def _env(n, a=0.004, d=0.12, sr=SR):
    t = np.arange(n) / sr
    e = np.minimum(1.0, t / max(a, 1e-4)) * np.exp(-np.maximum(0, t - a) / max(d, 1e-4))
    return e


def _noise(n, seed=0):
    return np.random.default_rng(seed).standard_normal(n)


def _band(x, lo, hi, sr=SR, order=2):
    sos = butter(order, [lo / (sr / 2), min(hi / (sr / 2), 0.99)], btype="band", output="sos")
    return sosfilt(sos, x)


def pop(dur=0.14, f0=900, f1=320):
    n = int(dur * SR)
    t = np.arange(n) / SR
    fr = f1 + (f0 - f1) * np.exp(-t * 40)
    ph = 2 * np.pi * np.cumsum(fr) / SR
    return 0.6 * np.sin(ph) * _env(n, 0.002, 0.045)


def whoosh(dur=0.6, up=True, seed=1):
    n = int(dur * SR)
    x = _noise(n, seed)
    out = np.zeros(n)
    steps = 24
    for k in range(steps):
        a, b = k * n // steps, (k + 1) * n // steps
        p = k / steps if up else 1 - k / steps
        c = 400 + 3200 * p
        out[a:b] = _band(x, c * 0.7, c * 1.3)[a:b]
    t = np.linspace(0, 1, n)
    return 0.5 * out * np.sin(np.pi * t) ** 1.5


def cash(dur=0.9):
    n = int(dur * SR)
    t = np.arange(n) / SR
    bell = sum(np.sin(2 * np.pi * f * t) * g for f, g in ((2093, 0.5), (2637, 0.35), (3136, 0.25), (4186, 0.12)))
    bell *= _env(n, 0.003, 0.35)
    click = _band(_noise(n, 4), 1500, 6000) * _env(n, 0.001, 0.02)
    out = 0.35 * bell + 0.5 * click
    d = int(0.09 * SR)
    out[d:] += 0.25 * bell[:-d]
    return out


def thud(dur=0.35):
    n = int(dur * SR)
    t = np.arange(n) / SR
    body = np.sin(2 * np.pi * (90 + 60 * np.exp(-t * 30)) * t) * _env(n, 0.002, 0.09)
    paper = _band(_noise(n, 9), 800, 5000) * _env(n, 0.001, 0.04)
    return 0.8 * body + 0.35 * paper


def flip(dur=0.08, seed=2):
    n = int(dur * SR)
    return 0.45 * _band(_noise(n, seed), 1200, 7000) * _env(n, 0.001, 0.025)


def tick(dur=0.03, seed=3):
    n = int(dur * SR)
    return 0.18 * _band(_noise(n, seed), 2500, 9000) * _env(n, 0.0005, 0.008)


def sparkle(dur=1.2, seed=5):
    n = int(dur * SR)
    out = np.zeros(n)
    rng = np.random.default_rng(seed)
    t = np.arange(n) / SR
    for _ in range(14):
        st = int(rng.uniform(0, dur * 0.8) * SR)
        f = rng.uniform(2500, 5200)
        m = n - st
        out[st:] += np.sin(2 * np.pi * f * t[:m]) * _env(m, 0.001, 0.08) * 0.12
    return out


def door(dur=0.9):
    n = int(dur * SR)
    x = whoosh(dur, up=True, seed=7) * 0.6
    t = np.arange(n) / SR
    shimmer = sum(np.sin(2 * np.pi * f * t) for f in (523, 659, 784, 1046)) * 0.06
    shimmer *= np.minimum(1, t / 0.4) * np.exp(-np.maximum(0, t - 0.4) * 3)
    return x + shimmer


def boing(dur=0.35):
    n = int(dur * SR)
    t = np.arange(n) / SR
    fr = 220 + 140 * np.sin(2 * np.pi * 9 * t) * np.exp(-t * 6)
    return 0.4 * np.sin(2 * np.pi * np.cumsum(fr) / SR) * _env(n, 0.003, 0.2)


def riser(dur=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    fr = 200 * (1 + 3 * t / dur) ** 1.2
    tone = np.sin(2 * np.pi * np.cumsum(fr) / SR) * 0.12 * (t / dur)
    return tone + whoosh(dur, True, 11) * 0.5


def pad_bed(duration, bpm=84, gain=0.05, chords=((0, 4, 7), (-3, 0, 4), (-7, -3, 0), (-5, -1, 2))):
    """Very soft sine/triangle pad (I-vi-IV-V in C), 2 bars per chord, slow attack/release."""
    n = int(duration * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    bar = 4 * 60 / bpm
    seg = 2 * bar
    k = 0
    while k * seg < duration:
        a, b = int(k * seg * SR), min(n, int((k + 1) * seg * SR) + int(0.6 * SR))
        tt = t[a:b] - k * seg
        env = np.minimum(1, tt / 0.9) * np.minimum(1, np.maximum(0, (seg + 0.6 - tt)) / 0.9)
        for semi in chords[k % len(chords)]:
            fr = 261.63 * 2 ** (semi / 12)
            out[a:b] += (np.sin(2 * np.pi * fr * tt) + 0.25 * np.sin(2 * np.pi * 2 * fr * tt)) * env
        root = 130.81 * 2 ** (chords[k % len(chords)][0] / 12)
        out[a:b] += 0.6 * np.sin(2 * np.pi * root * tt) * env
        k += 1
    sos = butter(2, 1800 / (SR / 2), btype="low", output="sos")
    return gain * sosfilt(sos, out) / 3.0


LIB = {"pop": pop, "whoosh": whoosh, "whoosh_down": lambda: whoosh(0.5, False, 3), "cash": cash, "thud": thud,
       "flip": flip, "tick": tick, "sparkle": sparkle, "door": door, "boing": boing, "riser": riser}


def mix(vo_wav: str, cues: list, out_wav: str, bed: bool = True, bed_gain=0.05, sfx_gain_db=-9.0,
        duck_db=-6.0):
    """cues = [(time_s, name, gain_db)]. VO is the reference; SFX at sfx_gain_db + cue gain.
    The bed is ducked under the VO (simple envelope follower)."""
    from .vo import loudnorm
    vo, sr = sf.read(vo_wav, dtype="float64")
    if vo.ndim > 1:
        vo = vo.mean(axis=1)
    assert sr == SR, f"VO must be {SR} Hz"
    n = vo.size
    fx = np.zeros(n)
    for (tm, name, g) in cues:
        snd = LIB[name]()
        a = int(tm * SR)
        if a >= n:
            continue
        b = min(n, a + snd.size)
        fx[a:b] += snd[: b - a] * 10 ** ((sfx_gain_db + g) / 20)
    out = vo + fx
    if bed:
        pad = pad_bed(n / SR, gain=bed_gain)[:n]
        envv = np.convolve(np.abs(vo), np.ones(int(0.25 * SR)) / int(0.25 * SR), mode="same")
        envv = envv / (envv.max() + 1e-9)
        duck = 10 ** ((duck_db * np.clip(envv * 4, 0, 1)) / 20)
        out = out + pad * duck
    tmp = out_wav + ".pre.wav"
    sf.write(tmp, out.astype(np.float32), SR, subtype="FLOAT")
    stats = loudnorm(tmp, out_wav)
    os.remove(tmp)
    return stats
