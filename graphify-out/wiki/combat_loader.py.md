# combat_loader.py

> 57 nodes

## Key Concepts

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
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- **test_combat_helpers.py** (6 connections) — `server/tests/unit/commands/test_combat_helpers.py`
- **asyncio** (6 connections)
- **test_handle_attack_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_flee_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_kick_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_punch_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_strike_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_taunt_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- *... and 32 more nodes in this community*

## Relationships

- [CombatCommandHandler](CombatCommandHandler.md) (11 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (4 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [CombatValidator](CombatValidator.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_helpers.py`
- `server/tests/unit/commands/test_combat_loader.py`

## Audit Trail

- EXTRACTED: 136 (86%)
- INFERRED: 22 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*