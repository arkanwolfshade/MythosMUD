# Container Sync Remediation

> 45 nodes

## Key Concepts

- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **handle_drop_command()** (15 connections) — `server/commands/inventory_drop_command.py`
- **handle_put_command()** (13 connections) — `server/commands/inventory_put_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **_put_resolve_container_id()** (9 connections) — `server/commands/inventory_put_command.py`
- **_put_transfer_finish()** (8 connections) — `server/commands/inventory_put_command.py`
- **CommandResponse** (7 connections)
- **_put_run_validated()** (7 connections) — `server/commands/inventory_put_command.py`
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_finish_after_persist()** (6 connections) — `server/commands/inventory_drop_command.py`
- **remove_item_from_inventory()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **_drop_quantity_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_inventory_rows_after_drop()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_slot_index_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_quantity_bounds_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **PutCommandRuntime** (4 connections) — `server/commands/inventory_put_command.py`
- **PutValidatedWork** (4 connections) — `server/commands/inventory_put_command.py`
- **CommandResponse** (4 connections)
- **Player** (3 connections)
- **UUID** (3 connections)
- **test_handle_drop_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- *... and 20 more nodes in this community*

## Relationships

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (20 shared connections)
- [Client Event Store](Client_Event_Store.md) (14 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (10 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (10 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (4 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (4 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (3 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)
- [NPC Room Event Handlers](NPC_Room_Event_Handlers.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 231 (92%)
- INFERRED: 19 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*