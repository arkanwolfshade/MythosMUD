# CorruptionService

> 33 nodes

## Key Concepts

- **CorruptionService** (42 connections) — `server/services/corruption_service.py`
- **test_corruption_service.py** (25 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_async_session_gen()** (14 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_player()** (13 connections) — `server/tests/unit/services/test_corruption_service.py`
- **asyncio** (13 connections)
- **test_apply_corruption_adjustment_bypass_permanence_floor_allows_zero()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_floors_at_1_once_touched()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_first_taint()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_tier_crossing()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_pushes_a_player_update_event()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_stays_at_0_when_never_touched()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_writes_through_the_tier_cache()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_clamps_to_100()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_no_notification_within_a_tier()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_positive_delta()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_allows_after_cooldown_expires()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_cleanse_reduces_corruption()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_rejects_on_cooldown()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **_clear_tier_cache()** (3 connections) — `server/tests/unit/services/test_corruption_service.py`
- **fixture** (3 connections)
- **.__init__()** (2 connections) — `server/services/corruption_service.py`
- **mock_repo()** (2 connections) — `server/tests/unit/services/test_corruption_service.py`
- **persistence()** (2 connections) — `server/tests/unit/services/test_corruption_service.py`
- **parametrize** (1 connections)
- **High-level operations for corruption adjustments. The single write path for…** (1 connections) — `server/services/corruption_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [cleanse_command.py](cleanse_command.py.md) (10 shared connections)
- [CorruptionTier](CorruptionTier.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (2 shared connections)
- [SpellLearningService](SpellLearningService.md) (2 shared connections)
- [passive_corruption_flux/service.py](passive_corruption_flux-service.py.md) (2 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (1 shared connections)
- [PlayerRespawnWrapper](PlayerRespawnWrapper.md) (1 shared connections)
- [CorruptionRepository](CorruptionRepository.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/services/corruption_service.py`
- `server/tests/unit/services/test_corruption_service.py`

## Audit Trail

- EXTRACTED: 99 (82%)
- INFERRED: 21 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*