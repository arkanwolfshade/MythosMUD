"""
Lightweight cache benchmark for CI artifacts.

Measures miss vs. hit timings for RoomCacheService with a fake persistence
that simulates I/O latency. Outputs JSON metrics to artifacts/perf/cache_bench.json.
"""

from __future__ import annotations

import asyncio
import json
import os
import time
from typing import Any


class _FakePersistence:
    """Fake persistence layer providing async_get_room with simulated latency."""

    def __init__(self, latency_ms: float = 5.0) -> None:
        self._latency = latency_ms / 1000.0

    async def async_get_room(self, room_id: str) -> dict[str, Any] | None:
        await asyncio.sleep(self._latency)
        # Return a minimal room dict
        return {
            "id": room_id,
            "name": f"Room {room_id}",
            "description": "Benchmark room",
            "exits": {},
        }


async def bench_room_cache() -> dict[str, Any]:
    from server.caching.cache_service import RoomCacheService  # local import

    persistence = _FakePersistence(latency_ms=5.0)
    cache_service = RoomCacheService(persistence)

    room_id = "bench_room_001"

    # Miss
    t0 = time.perf_counter()
    _ = await cache_service.get_room(room_id)
    t1 = time.perf_counter()

    # Hit
    t2 = time.perf_counter()
    _ = await cache_service.get_room(room_id)
    t3 = time.perf_counter()

    miss_ms = round((t1 - t0) * 1000.0, 3)
    hit_ms = round((t3 - t2) * 1000.0, 3)

    return {
        "suite": "cache_bench",
        "room_id": room_id,
        "miss_ms": miss_ms,
        "hit_ms": hit_ms,
        "speedup": round((miss_ms / hit_ms) if hit_ms > 0 else 0.0, 3),
    }


def main() -> None:
    metrics = asyncio.run(bench_room_cache())

    out_dir = os.path.join("artifacts", "perf")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cache_bench.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    print(json.dumps(metrics))


if __name__ == "__main__":
    main()
