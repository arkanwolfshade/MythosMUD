# Community 297

> 54 nodes

## Key Concepts

- **CorruptionRepository** (18 connections) — `server/services/corruption_repository.py`
- **test_corruption_repository.py** (14 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **_MockAsyncSession** (10 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **.apply_corruption_adjustment()** (10 connections) — `server/services/corruption_service.py`
- **.perform_recovery_action()** (10 connections) — `server/services/corruption_service.py`
- **corruption_repository.py** (10 connections) — `server/services/corruption_repository.py`
- **CorruptionUpdateResult** (7 connections) — `server/services/corruption_service.py`
- **.get_cooldown_expiry()** (7 connections) — `server/services/corruption_service.py`
- **test_get_cooldown_returns_record()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_set_cooldown_updates_existing()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **UUID** (7 connections)
- **.set_cooldown()** (6 connections) — `server/services/corruption_repository.py`
- **._notify_tier_crossing()** (6 connections) — `server/services/corruption_service.py`
- **_scalar_result()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_get_cooldown_returns_none_when_absent()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_set_cooldown_creates_when_absent()** (6 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/corruption_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/corruption_repository.py`
- **._send_corruption_update_event()** (5 connections) — `server/services/corruption_service.py`
- **repo()** (5 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_add_adjustment_log()** (5 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **asyncio** (5 connections)
- **_utc_now()** (4 connections) — `server/services/corruption_repository.py`
- **mock_session()** (4 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **UUID** (4 connections)
- *... and 29 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (15 shared connections)
- [Community 520](Community_520.md) (6 shared connections)
- [Community 172](Community_172.md) (3 shared connections)
- [Community 161](Community_161.md) (3 shared connections)
- [Community 783](Community_783.md) (2 shared connections)
- [Community 58](Community_58.md) (1 shared connections)
- [Community 160](Community_160.md) (1 shared connections)
- [Community 499](Community_499.md) (1 shared connections)
- [Community 514](Community_514.md) (1 shared connections)

## Source Files

- `server/services/corruption_repository.py`
- `server/services/corruption_service.py`
- `server/tests/unit/services/test_corruption_repository.py`

## Audit Trail

- EXTRACTED: 110 (89%)
- INFERRED: 13 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*