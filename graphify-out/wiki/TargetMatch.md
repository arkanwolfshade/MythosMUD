# TargetMatch

> 151 nodes · cohesion 0.03

## Key Concepts

- **command_result_text()** (52 connections) — `server/tests/unit/commands/inventory_commands_test_support.py`
- **inventory_equip_command.py** (50 connections) — `server/commands/inventory_equip_command.py`
- **server/services/__init__.py** (43 connections) — `server/services/__init__.py`
- **test_inventory_equip_command.py** (36 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **get_shared_services()** (21 connections) — `server/commands/inventory_service_helpers.py`
- **SlotValidationError** (21 connections) — `server/services/equipment_service.py`
- **test_inventory_commands.py** (21 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **handle_equip_command()** (16 connections) — `server/commands/inventory_equip_command.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **asyncio** (15 connections)
- **_equip_build_work()** (14 connections) — `server/commands/inventory_equip_command.py`
- **_sample_work()** (13 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **_equip_run_mutation()** (12 connections) — `server/commands/inventory_equip_command.py`
- **EquipmentCapacityError** (11 connections) — `server/services/equipment_service.py`
- **handle_wearable_container_on_equip()** (10 connections) — `server/commands/equipment_helpers.py`
- **normalize_inventory_slots()** (10 connections) — `server/commands/equipment_helpers.py`
- **_equip_success_payload()** (10 connections) — `server/commands/inventory_equip_command.py`
- **.equip_from_inventory()** (10 connections) — `server/services/equipment_service.py`
- **asyncio** (10 connections)
- **_equip_target_slot_or_error()** (9 connections) — `server/commands/inventory_equip_command.py`
- **_ensure_shared_services_initialized()** (9 connections) — `server/commands/inventory_service_helpers.py`
- **_equip_persist_or_rollback()** (8 connections) — `server/commands/inventory_equip_command.py`
- *... and 126 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (37 shared connections)
- [test_command_alias.py](test_command_alias.py.md) (19 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (16 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (14 shared connections)
- [validate_calendar.py](validate_calendar.py.md) (13 shared connections)
- [command_parser.py](command_parser.py.md) (11 shared connections)
- [deprecated_patterns.py](deprecated_patterns.py.md) (11 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (9 shared connections)
- [Protocol](Protocol.md) (8 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (7 shared connections)
- [Room](Room.md) (6 shared connections)
- [SuccessLevel](SuccessLevel.md) (5 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_service_helpers.py`
- `server/services/__init__.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/inventory_commands_test_support.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 472 (92%)
- INFERRED: 41 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*