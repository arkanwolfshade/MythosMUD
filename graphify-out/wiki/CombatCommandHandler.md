# CombatCommandHandler

> 90 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **test_combat_handler.py** (38 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **asyncio** (12 connections)
- **_as_app_with_state()** (9 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_current_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **test_resolve_combat_target_rejects_dead_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_non_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppStatePersistence** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- **test_get_player_and_room_no_persistence_on_app()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_failure_message()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **test_combat_command_handler_extras_optional()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_handle_flee_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 65 more nodes in this community*

## Relationships

- [combat_loader.py](combat_loader.py.md) (8 shared connections)
- [TargetType](TargetType.md) (8 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (6 shared connections)
- [TargetMatch](TargetMatch.md) (6 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [test_combat_grace_period.py](test_combat_grace_period.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [CombatValidator](CombatValidator.md) (2 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/commands/test_combat_handler.py`

## Audit Trail

- EXTRACTED: 173 (86%)
- INFERRED: 29 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*