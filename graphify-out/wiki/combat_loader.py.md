# combat_loader.py

> 39 nodes

## Key Concepts

- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **_app_from_request()** (8 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (7 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (7 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (7 connections) — `server/commands/combat_loader.py`
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **handle_attack_command()** (6 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (6 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (6 connections) — `server/commands/combat_loader.py`
- **test_combat_helpers.py** (6 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **test_format_combat_status_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_format_combat_status_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **test_get_combat_target_not_found()** (3 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **Any** (2 connections)
- **Movement service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Player position service for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Produce a human-readable combat status string. This helper is retained for…** (1 connections) — `server/commands/combat_helpers.py`
- **Resolve a combat target by name. The current implementation is intentionally…** (1 connections) — `server/commands/combat_helpers.py`
- **Combat command handler singleton and public async command entry points.…** (1 connections) — `server/commands/combat_loader.py`
- *... and 14 more nodes in this community*

## Relationships

- [PlayerCombatService](PlayerCombatService.md) (13 shared connections)
- [AliasStorage](AliasStorage.md) (11 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (4 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [test_player_schema_converter_weapon.py](test_player_schema_converter_weapon.py.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_helpers.py`

## Audit Trail

- EXTRACTED: 146 (87%)
- INFERRED: 21 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*