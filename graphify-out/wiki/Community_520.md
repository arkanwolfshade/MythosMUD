# Community 520

> 33 nodes

## Key Concepts

- **CorruptionService** (42 connections) — `server/services/corruption_service.py`
- **test_corruption_service.py** (25 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_async_session_gen()** (14 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_player()** (13 connections) — `server/tests/unit/services/test_corruption_service.py`
- **asyncio** (13 connections)
- **test_apply_corruption_adjustment_bypass_permanence_floor_allows_zero()** (8 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_floors_at_1_once_touched()** (8 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_first_taint()** (8 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_tier_crossing()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_pushes_a_player_update_event()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_stays_at_0_when_never_touched()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_writes_through_the_tier_cache()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_clamps_to_100()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_no_notification_within_a_tier()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_positive_delta()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_allows_after_cooldown_expires()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_cleanse_reduces_corruption()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_rejects_on_cooldown()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_clear_tier_cache()** (3 connections) — `server/tests/unit/services/test_corruption_service.py`
- **fixture** (3 connections)
- **.__init__()** (2 connections) — `server/services/corruption_service.py`
- **mock_repo()** (2 connections) — `server/tests/unit/services/test_corruption_service.py`
- **persistence()** (2 connections) — `server/tests/unit/services/test_corruption_service.py`
- **parametrize** (1 connections)
- **High-level operations for corruption adjustments. The single write path for…** (1 connections) — `server/services/corruption_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [Community 38](Community_38.md) (13 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (7 shared connections)
- [Community 297](Community_297.md) (6 shared connections)
- [Community 114](Community_114.md) (5 shared connections)
- [Community 783](Community_783.md) (3 shared connections)
- [Community 423](Community_423.md) (2 shared connections)
- [Community 110](Community_110.md) (2 shared connections)
- [Community 68](Community_68.md) (2 shared connections)
- [Community 374](Community_374.md) (2 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (2 shared connections)
- [Community 172](Community_172.md) (2 shared connections)
- [Community 514](Community_514.md) (2 shared connections)

## Source Files

- `server/services/corruption_service.py`
- `server/tests/unit/services/test_corruption_service.py`

## Audit Trail

- EXTRACTED: 99 (74%)
- INFERRED: 34 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*