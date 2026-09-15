# CorruptionRepository

> 35 nodes

## Key Concepts

- **CorruptionRepository** (18 connections) — `server/services/corruption_repository.py`
- **_MockAsyncSession** (10 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_get_cooldown_returns_record()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_set_cooldown_updates_existing()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/corruption_repository.py`
- **_scalar_result()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_get_cooldown_returns_none_when_absent()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_set_cooldown_creates_when_absent()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/corruption_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/corruption_repository.py`
- **repo()** (5 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_add_adjustment_log()** (5 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **asyncio** (5 connections)
- **_utc_now()** (4 connections) — `server/services/corruption_repository.py`
- **mock_session()** (4 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **UUID** (4 connections)
- **datetime** (3 connections)
- **.__init__()** (2 connections) — `server/services/corruption_repository.py`
- **fixture** (2 connections)
- **.__init__()** (1 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **AsyncSession** (1 connections)
- **Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE.** (1 connections) — `server/services/corruption_repository.py`
- **Data-access helpers for corruption persistence. Mirrors `LucidityRepository`.** (1 connections) — `server/services/corruption_repository.py`
- **Add a corruption adjustment log entry.** (1 connections) — `server/services/corruption_repository.py`
- **Get cooldown state for a player and action.** (1 connections) — `server/services/corruption_repository.py`
- *... and 10 more nodes in this community*

## Relationships

- [Player](Player.md) (19 shared connections)
- [cleanse_command.py](cleanse_command.py.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [CorruptionService](CorruptionService.md) (1 shared connections)

## Source Files

- `server/services/corruption_repository.py`
- `server/tests/unit/services/test_corruption_repository.py`

## Audit Trail

- EXTRACTED: 67 (89%)
- INFERRED: 8 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*