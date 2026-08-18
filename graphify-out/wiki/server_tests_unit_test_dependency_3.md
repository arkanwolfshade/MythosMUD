# server tests unit test dependency

> 6 nodes

## Key Concepts

- **TestGetStatsGenerator** (5 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_stats_generator() function.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_stats_generator() returns StatsGenerator instance.** (1 connections) — `server/tests/unit/test_dependency_injection.py`
- **Test get_stats_generator() returns stateless instance.** (1 connections) — `server/tests/unit/test_dependency_injection.py`

## Relationships

- [server dependencies](server_dependencies.md) (3 shared connections)
- [computed field](computed_field.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*