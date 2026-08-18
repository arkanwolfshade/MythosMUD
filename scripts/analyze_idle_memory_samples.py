"""Analyze idle memory JSONL samples (warmup + measurement windows)."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import cast

WARMUP_SECONDS = 30 * 60
SLOPE_KEYS = (
    "rss_bytes",
    "heap_current_bytes",
    "heap_peak_bytes",
    "npc_pending_keys",
    "event_bus_queue",
    "perf_metrics",
    "perf_operation_keys",
    "perf_operation_metrics",
    "log_hour_keys",
    "asyncio_tasks",
)


class JsonSample(dict[str, float | int]):
    """JSONL row with numeric fields used for slope analysis."""


def _slope_per_hour(samples: list[JsonSample], key: str) -> float:
    if len(samples) < 2:
        return 0.0
    t0 = float(samples[0]["ts"])
    xs = [(float(samples[i]["ts"]) - t0) / 3600.0 for i in range(len(samples))]
    ys = [float(samples[i][key]) for i in range(len(samples))]
    x_mean = sum(xs) / len(xs)
    y_mean = sum(ys) / len(ys)
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys, strict=True))
    den = sum((x - x_mean) ** 2 for x in xs)
    if den == 0:
        return 0.0
    return num / den


def _append_slope_rows(lines_out: list[str], measure: list[JsonSample]) -> None:
    first = measure[0]
    last = measure[-1]
    duration_h = (float(last["ts"]) - float(first["ts"])) / 3600.0
    lines_out.append(f"measure_duration_hours={duration_h:.2f}")
    for key in SLOPE_KEYS:
        slope = _slope_per_hour(measure, key)
        start_val = float(first[key])
        end_val = float(last[key])
        delta = end_val - start_val
        lines_out.append(
            f"{key}: start={start_val:.0f} end={end_val:.0f} delta={delta:.0f} slope_per_hour={slope:.2f}"
        )


def analyze(path: Path, warmup_seconds: int = WARMUP_SECONDS) -> str:
    samples = [
        cast(JsonSample, json.loads(line))
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not samples:
        return f"No samples in {path}"

    t0 = float(samples[0]["ts"])
    warmup_end = t0 + warmup_seconds
    measure = [s for s in samples if float(s["ts"]) >= warmup_end]
    warmup = [s for s in samples if float(s["ts"]) < warmup_end]
    lines_out = [
        f"file={path}",
        f"total_samples={len(samples)} warmup_samples={len(warmup)} measure_samples={len(measure)}",
        f"warmup_seconds={warmup_seconds}",
    ]
    if len(measure) < 2:
        lines_out.append("measurement window too short for slope analysis")
        return "\n".join(lines_out)
    _append_slope_rows(lines_out, measure)
    return "\n".join(lines_out)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: analyze_idle_memory_samples.py <path-to-jsonl>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"missing file: {path}", file=sys.stderr)
        return 1
    print(analyze(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
