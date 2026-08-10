# Review Code Postgresql

> 4 nodes

## Key Concepts

- **TestGetStatsGenerator** (4 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_stats_generator_returns_instance()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_stats_generator dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_stats_generator returns StatsGenerator instance.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*