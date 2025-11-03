"""
NPC cache micro-benchmark for CI artifacts.
Measures miss vs. hit timings for NPCCacheService using a fake NPC service.
Writes metrics to artifacts/perf/cache_bench_npc.json.
"""

from __future__ import annotations

import asyncio
import json
import os
import time
from types import SimpleNamespace
from typing import Any


class _FakeNPCService:
    def __init__(self, latency_ms: float = 5.0) -> None:
        self._latency = latency_ms / 1000.0

    async def get_npc_definitions(self, session: Any) -> list[Any]:
        await asyncio.sleep(self._latency)
        return [SimpleNamespace(id=i, name=f"NPC-{i}") for i in range(50)]

    async def get_npc_definition(self, session: Any, definition_id: int) -> Any:
        await asyncio.sleep(self._latency)
        return SimpleNamespace(id=definition_id, name=f"NPC-{definition_id}")

    async def get_spawn_rules(self, session: Any) -> list[Any]:
        await asyncio.sleep(self._latency)
        return [SimpleNamespace(id=i, rule="any") for i in range(25)]


async def bench_npc_cache() -> dict[str, Any]:
    from server.caching.cache_service import NPCCacheService  # local import

    npc_service = _FakeNPCService(latency_ms=5.0)
    cache = NPCCacheService(npc_service)

    # Definitions miss/hit
    t0 = time.perf_counter()
    await cache.get_npc_definitions(None)
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    await cache.get_npc_definitions(None)
    t3 = time.perf_counter()

    # Spawn rules miss/hit
    t4 = time.perf_counter()
    await cache.get_spawn_rules(None)
    t5 = time.perf_counter()
    t6 = time.perf_counter()
    await cache.get_spawn_rules(None)
    t7 = time.perf_counter()

    defs_miss_ms = round((t1 - t0) * 1000.0, 3)
    defs_hit_ms = round((t3 - t2) * 1000.0, 3)
    rules_miss_ms = round((t5 - t4) * 1000.0, 3)
    rules_hit_ms = round((t7 - t6) * 1000.0, 3)

    return {
        "suite": "cache_bench_npc",
        "defs_miss_ms": defs_miss_ms,
        "defs_hit_ms": defs_hit_ms,
        "defs_speedup": round((defs_miss_ms / defs_hit_ms) if defs_hit_ms > 0 else 0.0, 3),
        "rules_miss_ms": rules_miss_ms,
        "rules_hit_ms": rules_hit_ms,
        "rules_speedup": round((rules_miss_ms / rules_hit_ms) if rules_hit_ms > 0 else 0.0, 3),
    }


def main() -> None:
    metrics = asyncio.run(bench_npc_cache())
    out_dir = os.path.join("artifacts", "perf")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cache_bench_npc.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    print(json.dumps(metrics))


if __name__ == "__main__":
    main()
