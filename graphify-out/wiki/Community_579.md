# Community 579

> 30 nodes

## Key Concepts

- **test_corruption_service.py** (22 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_async_session_gen()** (14 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_player()** (13 connections) — `server/tests/unit/services/test_corruption_service.py`
- **asyncio** (13 connections)
- **test_apply_corruption_adjustment_floors_at_1_once_touched()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_bypass_permanence_floor_allows_zero()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_first_taint()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_pushes_a_player_update_event()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_stays_at_0_when_never_touched()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_writes_through_the_tier_cache()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_clamps_to_100()** (4 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_no_notification_within_a_tier()** (4 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_tier_crossing()** (4 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_positive_delta()** (4 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_allows_after_cooldown_expires()** (4 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_cleanse_reduces_corruption()** (4 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_clear_tier_cache()** (3 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_rejects_on_cooldown()** (3 connections) — `server/tests/unit/services/test_corruption_service.py`
- **fixture** (3 connections)
- **mock_repo()** (2 connections) — `server/tests/unit/services/test_corruption_service.py`
- **persistence()** (2 connections) — `server/tests/unit/services/test_corruption_service.py`
- **parametrize** (1 connections)
- **Unit tests for CorruptionService (#804).** (1 connections) — `server/tests/unit/services/test_corruption_service.py`
- **#815: a player who has never been corrupted has no floor -- 0 is a real,…** (1 connections) — `server/tests/unit/services/test_corruption_service.py`
- **#815: once corruption exceeds 0, this service can never take it back below 1.** (1 connections) — `server/tests/unit/services/test_corruption_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (1 shared connections)
- [Community 337](Community_337.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_corruption_service.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*