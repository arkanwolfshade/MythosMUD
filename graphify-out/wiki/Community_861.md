# Community 861

> 18 nodes

## Key Concepts

- **stats_generator_summary.py** (9 connections) — `server/game/stats_generator_summary.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **build_stat_summary()** (8 connections) — `server/game/stats_generator_summary.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **_build_attribute_summary()** (4 connections) — `server/game/stats_generator_summary.py`
- **_core_stat_values_by_field()** (4 connections) — `server/game/stats_generator_summary.py`
- **_stat_value_for_summary()** (3 connections) — `server/game/stats_generator_summary.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **Stats** (3 connections)
- **StrEnum** (3 connections)
- **Get a summary of the character's stats including modifiers and totals. Args:…** (1 connections) — `server/game/stats_generator.py`
- **Stat summary helpers for StatsGenerator (keeps stats_generator under module…** (1 connections) — `server/game/stats_generator_summary.py`
- **Coerce optional stat ints for summary totals (matches legacy ``or 50``…** (1 connections) — `server/game/stats_generator_summary.py`
- **Map core stat field names to current values (typed access, no getattr).** (1 connections) — `server/game/stats_generator_summary.py`
- **Build per-attribute value and modifier entries for stat summary.** (1 connections) — `server/game/stats_generator_summary.py`
- **Build full stat summary dict including modifiers, derived stats, and totals.** (1 connections) — `server/game/stats_generator_summary.py`
- **Get the modifier for a given attribute (standard D&D-style calculation).** (1 connections) — `server/models/game.py`
- **Core attribute types for the character system .** (1 connections) — `server/models/game.py`

## Relationships

- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (4 shared connections)
- [Community 236](Community_236.md) (3 shared connections)
- [Community 61](Community_61.md) (3 shared connections)
- [Community 391](Community_391.md) (2 shared connections)
- [Community 1090](Community_1090.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/game/stats_generator_summary.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*