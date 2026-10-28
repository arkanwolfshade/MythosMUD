# test_inventory_mutation_guard_error_handling.py

> 13 nodes · cohesion 0.22

## Key Concepts

- **stats_generator_summary.py** (9 connections) — `server/game/stats_generator_summary.py`
- **build_stat_summary()** (8 connections) — `server/game/stats_generator_summary.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **_build_attribute_summary()** (4 connections) — `server/game/stats_generator_summary.py`
- **_core_stat_values_by_field()** (4 connections) — `server/game/stats_generator_summary.py`
- **Stats** (3 connections)
- **_stat_value_for_summary()** (3 connections) — `server/game/stats_generator_summary.py`
- **Get a summary of the character's stats including modifiers and totals. Args:…** (1 connections) — `server/game/stats_generator.py`
- **Stat summary helpers for StatsGenerator (keeps stats_generator under module…** (1 connections) — `server/game/stats_generator_summary.py`
- **Coerce optional stat ints for summary totals (matches legacy ``or 50``…** (1 connections) — `server/game/stats_generator_summary.py`
- **Map core stat field names to current values (typed access, no getattr).** (1 connections) — `server/game/stats_generator_summary.py`
- **Build per-attribute value and modifier entries for stat summary.** (1 connections) — `server/game/stats_generator_summary.py`
- **Build full stat summary dict including modifiers, derived stats, and totals.** (1 connections) — `server/game/stats_generator_summary.py`

## Relationships

- [testing_examples.py](testing_examples.py.md) (4 shared connections)
- [test_rate_limiter.py](test_rate_limiter.py.md) (1 shared connections)
- [Improve Layout Systematically](Improve_Layout_Systematically.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/game/stats_generator_summary.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*