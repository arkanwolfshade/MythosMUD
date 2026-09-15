# TargetResolutionResult

> 79 nodes

## Key Concepts

- **TargetResolutionResult** (36 connections) — `server/schemas/shared/target_resolution.py`
- **.async_persistence()** (27 connections) — `server/commands/cleanse_command.py`
- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **follow_commands.py** (18 connections) — `server/commands/follow_commands.py`
- **handle_follow_command()** (17 connections) — `server/commands/follow_commands.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **asyncio** (13 connections)
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_following_command()** (11 connections) — `server/commands/follow_commands.py`
- **handle_unfollow_command()** (11 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_self_rejected()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_get_container()** (6 connections) — `server/commands/follow_commands.py`
- **_load_follow_context()** (6 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_no_persistence()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_target()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_player_not_in_game()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_display()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_success()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_was_not_following()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Any** (6 connections)
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- *... and 54 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (16 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (6 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [command_service.py](command_service.py.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [.resolve_target](resolve_target.md) (3 shared connections)
- [SpellEffectType](SpellEffectType.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [TargetType](TargetType.md) (3 shared connections)

## Source Files

- `server/commands/cleanse_command.py`
- `server/commands/combat_handler.py`
- `server/commands/follow_commands.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 197 (84%)
- INFERRED: 37 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*