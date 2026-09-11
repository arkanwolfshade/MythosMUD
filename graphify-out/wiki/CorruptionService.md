# CorruptionService

> 85 nodes

## Key Concepts

- **CorruptionService** (39 connections) — `server/services/corruption_service.py`
- **test_corruption_service.py** (24 connections) — `server/tests/unit/services/test_corruption_service.py`
- **cleanse_command.py** (23 connections) — `server/commands/cleanse_command.py`
- **CorruptionPersistenceProtocol** (15 connections) — `server/services/corruption_service.py`
- **handle_cleanse_command()** (14 connections) — `server/commands/cleanse_command.py`
- **_async_session_gen()** (13 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_cleanse_command.py** (13 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **_player()** (12 connections) — `server/tests/unit/services/test_corruption_service.py`
- **asyncio** (12 connections)
- **CorruptionPersistencePlayer** (11 connections) — `server/services/corruption_service.py`
- **CorruptionActionOnCooldownError** (10 connections) — `server/services/corruption_service.py`
- **CleansePersistence** (8 connections) — `server/commands/cleanse_command.py`
- **test_apply_corruption_adjustment_floors_at_1_once_touched()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_first_taint()** (7 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_notifies_on_tier_crossing()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_pushes_a_player_update_event()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_stays_at_0_when_never_touched()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_writes_through_the_tier_cache()** (6 connections) — `server/tests/unit/services/test_corruption_service.py`
- **Protocol** (6 connections)
- **CleanseTargetPlayer** (5 connections) — `server/commands/cleanse_command.py`
- **CorruptionActionError** (5 connections) — `server/services/corruption_service.py`
- **test_apply_corruption_adjustment_clamps_to_100()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_no_notification_within_a_tier()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_apply_corruption_adjustment_positive_delta()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- **test_perform_recovery_action_allows_after_cooldown_expires()** (5 connections) — `server/tests/unit/services/test_corruption_service.py`
- *... and 60 more nodes in this community*

## Relationships

- [Player](Player.md) (18 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [magic_service.py](magic_service.py.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [SpellLearningService](SpellLearningService.md) (5 shared connections)
- [CorruptionTier](CorruptionTier.md) (4 shared connections)
- [.async_persistence](async_persistence.md) (2 shared connections)
- [passive_corruption_flux/service.py](passive_corruption_flux-service.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/services/corruption_service.py`
- `server/tests/unit/commands/test_cleanse_command.py`
- `server/tests/unit/services/test_corruption_service.py`

## Audit Trail

- EXTRACTED: 199 (88%)
- INFERRED: 26 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*