# retry.py

> 39 nodes · cohesion 0.09

## Key Concepts

- **CorruptionRepository** (18 connections) — `server/services/corruption_repository.py`
- **test_corruption_repository.py** (14 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **corruption_repository.py** (10 connections) — `server/services/corruption_repository.py`
- **_MockAsyncSession** (10 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_get_cooldown_returns_record()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_set_cooldown_updates_existing()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/corruption_repository.py`
- **_scalar_result()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_get_cooldown_returns_none_when_absent()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_set_cooldown_creates_when_absent()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/corruption_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/corruption_repository.py`
- **asyncio** (5 connections)
- **repo()** (5 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_add_adjustment_log()** (5 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **UUID** (4 connections)
- **_utc_now()** (4 connections) — `server/services/corruption_repository.py`
- **mock_session()** (4 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **datetime** (3 connections)
- **.__init__()** (2 connections) — `server/services/corruption_repository.py`
- **fixture** (2 connections)
- **AsyncSession** (1 connections)
- **Repository layer for corruption ledger and cooldown persistence (#804).** (1 connections) — `server/services/corruption_repository.py`
- **Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE.** (1 connections) — `server/services/corruption_repository.py`
- **Data-access helpers for corruption persistence. Mirrors `LucidityRepository`.** (1 connections) — `server/services/corruption_repository.py`
- *... and 14 more nodes in this community*

## Relationships

- [fixtures/auth.ts](fixtures-auth.ts.md) (8 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (4 shared connections)
- [reset_database](reset_database.md) (4 shared connections)

## Source Files

- `server/services/corruption_repository.py`
- `server/tests/unit/services/test_corruption_repository.py`

## Audit Trail

- EXTRACTED: 76 (90%)
- INFERRED: 8 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*