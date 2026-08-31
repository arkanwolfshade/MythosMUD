# CombatCommandHandler

> 81 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (23 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **_app_from_request()** (11 connections) — `server/commands/combat_loader.py`
- **CombatCommandHandlerExtras** (9 connections) — `server/commands/combat_handler.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **handler()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **asyncio** (6 connections)
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **.combat_service()** (4 connections) — `server/commands/combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.get_npc_instance()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **test_combat_command_handler_extras_optional()** (4 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 56 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (16 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (10 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (10 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (5 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [format_combat_status](format_combat_status.md) (3 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_loader.py`
- `server/tests/unit/commands/test_flee_command.py`

## Audit Trail

- EXTRACTED: 191 (84%)
- INFERRED: 36 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*