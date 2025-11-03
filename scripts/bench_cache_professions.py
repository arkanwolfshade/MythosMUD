"""
Professions cache micro-benchmark for CI artifacts.
Measures miss vs. hit timings for ProfessionCacheService using a fake persistence.
Writes metrics to artifacts/perf/cache_bench_professions.json.
"""

from __future__ import annotations

import json
import os
import time
from types import SimpleNamespace
from typing import Any


def _get_empty_dict() -> dict[str, Any]:
    """Helper function to return empty dict for mock methods."""
    return {}


class _FakePersistence:
    def __init__(self, latency_ms: float = 5.0) -> None:
        self._latency = latency_ms / 1000.0

    def get_all_professions(self) -> list[Any]:
        import time as _t

        _t.sleep(self._latency)
        # Return mock Profession objects with .id attribute (not plain dicts)
        professions = []
        for i in range(20):
            # Create SimpleNamespace with methods that return empty dicts
            prof = SimpleNamespace(
                id=i,
                name=f"Profession-{i}",
                description=f"Description for Profession-{i}",
                flavor_text=f"Flavor text for Profession-{i}",
                stat_requirements="{}",
                mechanical_effects="{}",
                is_available=True,
            )
            # Add callable methods
            prof.get_stat_requirements = _get_empty_dict  # type: ignore[method-assign]
            prof.get_mechanical_effects = _get_empty_dict  # type: ignore[method-assign]
            professions.append(prof)
        return professions


def bench_profession_cache() -> dict[str, Any]:
    from server.caching.cache_service import ProfessionCacheService  # local import

    persistence = _FakePersistence(latency_ms=5.0)
    cache = ProfessionCacheService(persistence)

    # Miss
    t0 = time.perf_counter()
    _ = cache.get_all_professions()
    t1 = time.perf_counter()
    # Hit
    t2 = time.perf_counter()
    _ = cache.get_all_professions()
    t3 = time.perf_counter()

    miss_ms = round((t1 - t0) * 1000.0, 3)
    hit_ms = round((t3 - t2) * 1000.0, 3)

    return {
        "suite": "cache_bench_professions",
        "miss_ms": miss_ms,
        "hit_ms": hit_ms,
        "speedup": round((miss_ms / hit_ms) if hit_ms > 0 else 0.0, 3),
    }


def main() -> None:
    metrics = bench_profession_cache()
    out_dir = os.path.join("artifacts", "perf")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cache_bench_professions.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    print(json.dumps(metrics))


if __name__ == "__main__":
    main()
