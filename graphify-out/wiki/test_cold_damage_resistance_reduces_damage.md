# test_cold_damage_resistance_reduces_damage

> 5 nodes

## Key Concepts

- **test_cold_damage_resistance_reduces_damage()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **test_damage_defaults_current_dp_to_20_when_missing()** (4 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **asyncio** (2 connections)
- **Cold resistance should reduce incoming cold-type damage before persistence.** (1 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **Missing current_dp should use base investigator fallback to avoid inflated…** (1 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Relationships

- [HealthRepository](HealthRepository.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)

## Source Files

- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*