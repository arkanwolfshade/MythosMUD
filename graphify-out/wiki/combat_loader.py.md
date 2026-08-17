# combat_loader.py

> 42 nodes

## Key Concepts

- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (23 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **_app_from_request()** (12 connections) — `server/commands/combat_loader.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **asyncio** (6 connections)
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **test_handle_attack_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_flee_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_kick_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_punch_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_strike_command_sets_type()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_handle_taunt_command_delegates()** (4 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **.movement_service()** (3 connections) — `server/commands/combat_handler.py`
- **.player_position_service()** (3 connections) — `server/commands/combat_handler.py`
- **test_get_combat_command_handler_creates_singleton()** (3 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **reset_combat_handler()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **test_app_from_request_none()** (2 connections) — `server/tests/unit/commands/test_combat_loader.py`
- *... and 17 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (18 shared connections)
- [AliasStorage](AliasStorage.md) (15 shared connections)
- [format_combat_status](format_combat_status.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (2 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (2 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)
- [player_combat_service](player_combat_service.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_loader.py`

## Audit Trail

- EXTRACTED: 116 (84%)
- INFERRED: 22 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*