# TargetResolutionResult

> 75 nodes

## Key Concepts

- **TargetResolutionResult** (38 connections) — `server/schemas/shared/target_resolution.py`
- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **follow_commands.py** (18 connections) — `server/commands/follow_commands.py`
- **handle_follow_command()** (17 connections) — `server/commands/follow_commands.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **asyncio** (13 connections)
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
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
- **target_metadata.py** (5 connections) — `server/schemas/shared/target_metadata.py`
- **_resolve_follow_target()** (4 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_no_container()** (4 connections) — `server/tests/unit/commands/test_follow_commands.py`
- *... and 50 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (16 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (13 shared connections)
- [command_service.py](command_service.py.md) (11 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (9 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [SpellEffectType](SpellEffectType.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (2 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 193 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*