# test_connection_establishment.py

> 125 nodes · cohesion 0.03

## Key Concepts

- **rescue_commands.py** (45 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (38 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **handle_ground_command()** (30 connections) — `server/commands/rescue_commands.py`
- **asyncio** (20 connections)
- **ground_commands_test_support.py** (18 connections) — `server/tests/unit/commands/ground_commands_test_support.py`
- **_ground_rig()** (15 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **FakeSession** (11 connections) — `server/tests/unit/commands/ground_commands_test_support.py`
- **_finish_ground()** (10 connections) — `server/commands/rescue_commands.py`
- **_run_ground()** (10 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **_apply_grounding_adjustment()** (9 connections) — `server/commands/rescue_commands.py`
- **_GroundRig** (9 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **FakePersistence** (8 connections) — `server/tests/unit/commands/ground_commands_test_support.py`
- **FakePlayer** (7 connections) — `server/tests/unit/commands/ground_commands_test_support.py`
- **ground_request()** (7 connections) — `server/tests/unit/commands/ground_commands_test_support.py`
- **_GroundContext** (6 connections) — `server/commands/rescue_commands.py`
- **_GroundPersistence** (6 connections) — `server/commands/rescue_commands.py`
- **_GroundPlayer** (6 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (6 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_target()** (6 connections) — `server/commands/rescue_commands.py`
- **FakeLucidityService** (6 connections) — `server/tests/unit/commands/ground_commands_test_support.py`
- **patch** (6 connections)
- **test_handle_ground_command_apply_lucidity_error()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_rejects_while_in_combat()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 100 more nodes in this community*

## Relationships

- [PopulationStats](PopulationStats.md) (17 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (16 shared connections)
- [command_parser.py](command_parser.py.md) (8 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (5 shared connections)
- [ItemFactory](ItemFactory.md) (4 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (3 shared connections)
- [test_command_registry_consistency.py](test_command_registry_consistency.py.md) (3 shared connections)
- [PlayerCombatState](PlayerCombatState.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [.load_room_data](load_room_data.md) (2 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/ground_commands_test_support.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 284 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*