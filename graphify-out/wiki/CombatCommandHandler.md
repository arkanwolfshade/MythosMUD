# CombatCommandHandler

> 134 nodes

## Key Concepts

- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (22 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **asyncio** (12 connections)
- **_app_from_request()** (11 connections) — `server/commands/combat_loader.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_get_player_and_room_no_current_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 109 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (20 shared connections)
- [TargetMatch](TargetMatch.md) (19 shared connections)
- [AliasStorage](AliasStorage.md) (16 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (9 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (9 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [test_combat_grace_period.py](test_combat_grace_period.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [format_combat_status](format_combat_status.md) (3 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_loader.py`

## Audit Trail

- EXTRACTED: 300 (83%)
- INFERRED: 60 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*