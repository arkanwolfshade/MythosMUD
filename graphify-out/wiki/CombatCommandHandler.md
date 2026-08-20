# CombatCommandHandler

> 48 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- **.combat_service()** (4 connections) — `server/commands/combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.get_npc_instance()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **test_combat_command_handler_extras_optional()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **Any** (4 connections)
- **.get_room_data()** (3 connections) — `server/commands/combat_handler.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **.room_forbids_combat()** (3 connections) — `server/commands/combat_handler.py`
- **.validate_combat_action()** (3 connections) — `server/commands/combat_handler.py`
- **.validate_target_name()** (3 connections) — `server/commands/combat_handler.py`
- **test_combat_command_handler_requires_async_persistence()** (3 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **AppWithState** (3 connections)
- **Combat service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Movement service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Player position service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Extract command type and target name from command_data. Public API.** (1 connections) — `server/commands/combat_handler.py`
- *... and 23 more nodes in this community*

## Relationships

- [combat_loader.py](combat_loader.py.md) (7 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (6 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (2 shared connections)
- [CombatValidator](CombatValidator.md) (2 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (2 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/commands/test_combat_handler.py`

## Audit Trail

- EXTRACTED: 83 (80%)
- INFERRED: 21 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*