# FastAPI Auth Integration

> 36 nodes

## Key Concepts

- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **handle_get_command()** (14 connections) — `server/commands/inventory_get_command.py`
- **_handle_get_from_room()** (13 connections) — `server/commands/inventory_get_command.py`
- **_get_from_container_path()** (12 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **GetCommandRuntime** (9 connections) — `server/commands/inventory_get_command.py`
- **GetItemSpec** (9 connections) — `server/commands/inventory_get_command.py`
- **FloorPickupEnvironment** (9 connections) — `server/commands/inventory_pickup_command.py`
- **FloorPickupPayload** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_get_transfer_out_of_container()** (7 connections) — `server/commands/inventory_get_command.py`
- **_get_route_after_validation()** (7 connections) — `server/commands/inventory_get_command.py`
- **inventory_command_coercion.py** (6 connections) — `server/commands/inventory_command_coercion.py`
- **CommandResponse** (5 connections)
- **UUID** (3 connections)
- **.__init__()** (3 connections) — `server/commands/inventory_pickup_command.py`
- **test_handle_get_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **.add_room_drop()** (2 connections) — `server/commands/inventory_command_contracts.py`
- **Player** (2 connections)
- **_container_transfer_messages()** (2 connections) — `server/commands/inventory_get_command.py`
- **test_handle_get_command_room_quantity_string_coerces_without_type_error()** (2 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Parse numeric fields from object-typed JSON command payloads.** (1 connections) — `server/commands/inventory_command_coercion.py`
- **Protocol** (1 connections)
- **.list_room_drops()** (1 connections) — `server/commands/inventory_command_contracts.py`
- **.take_room_drop()** (1 connections) — `server/commands/inventory_command_contracts.py`
- *... and 11 more nodes in this community*

## Relationships

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (15 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (10 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (6 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (3 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 149 (78%)
- INFERRED: 41 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*