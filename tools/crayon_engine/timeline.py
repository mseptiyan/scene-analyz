"""Timeline: shots whose hard cuts are locked to VO word timestamps.

Reference rule (wolf_frame_analysis §3.3): one phrase = one shot, and the cut lands 0.1-0.3 s
*before* the phrase starts (median 0.22 s). `Words.cut()` returns exactly that.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Callable

from .core import Camera


def _n(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


class Words:
    def __init__(self, words_json: str, lines_json: str):
        self.words = json.load(open(words_json))
        self.lines = {str(l["id"]): l for l in json.load(open(lines_json))}

    def of_line(self, line_id):
        return [w for w in self.words if str(w["line"]) == str(line_id)]

    def find(self, line_id, token=None, nth: int = 0):
        ws = self.of_line(line_id)
        if token is None:
            return ws[0]
        hits = [w for w in ws if _n(w["word"]).startswith(_n(token))]
        if not hits:
            raise KeyError(f"word '{token}' not in line {line_id}: {[w['word'] for w in ws]}")
        return hits[nth]

    def t(self, line_id, token=None, nth=0, end=False) -> float:
        w = self.find(line_id, token, nth)
        return w["end"] if end else w["start"]

    def cut(self, line_id, token=None, lead: float = 0.2, nth=0) -> float:
        return max(0.0, self.t(line_id, token, nth) - lead)

    def line(self, line_id):
        return self.lines[str(line_id)]


@dataclass
class Shot:
    id: str
    draw: Callable
    start: float = 0.0
    cam: Camera | Callable | None = None
    meta: dict = field(default_factory=dict)  # shot-list fields (size, cam, action, expr, text, sfx, trans)
    end: float = 0.0                          # set by Timeline from the next shot's start

    @property
    def dur(self):
        return self.end - self.start

    def camera(self) -> Camera:
        if self.cam is None:
            return Camera()
        return self.cam(self.dur) if callable(self.cam) else self.cam


class Timeline:
    def __init__(self, shots: list[Shot], total: float):
        self.shots = shots
        self.total = total
        for i, s in enumerate(shots):
            s.end = shots[i + 1].start if i + 1 < len(shots) else total
            if s.end <= s.start:
                raise ValueError(f"shot {s.id} has non-positive duration ({s.start}->{s.end})")

    def at(self, T: float) -> Shot:
        for s in self.shots:
            if s.start <= T < s.end:
                return s
        return self.shots[-1]
