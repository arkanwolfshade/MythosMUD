# TargetType

> 95 nodes

## Key Concepts

- **TargetType** (41 connections) — `server/schemas/shared/target_resolution.py`
- **TargetResolutionResult** (34 connections) — `server/schemas/shared/target_resolution.py`
- **test_spell_targeting.py** (29 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_follow_commands.py** (24 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **follow_commands.py** (18 connections) — `server/commands/follow_commands.py`
- **handle_follow_command()** (17 connections) — `server/commands/follow_commands.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **asyncio** (13 connections)
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **target_resolution.py** (12 connections) — `server/schemas/shared/target_resolution.py`
- **handle_following_command()** (10 connections) — `server/commands/follow_commands.py`
- **handle_unfollow_command()** (10 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_self_rejected()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_get_container()** (7 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **asyncio** (7 connections)
- **test_handle_follow_no_persistence()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_target()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_player_not_in_game()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_display()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_success()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_was_not_following()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- *... and 70 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (22 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (14 shared connections)
- [Spell](Spell.md) (13 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (8 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 279 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*