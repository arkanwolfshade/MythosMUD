# Community 332

> 50 nodes

## Key Concepts

- **emit_inventory_updated()** (26 connections) — `server/services/inventory_websocket_events.py`
- **inventory_drop_command.py** (21 connections) — `server/commands/inventory_drop_command.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **_drop_resolve_stack_or_error()** (9 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_websocket_events.py** (9 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **_Owner** (8 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **CommandResponse** (7 connections)
- **_InventoryOwner** (6 connections) — `server/services/inventory_websocket_events.py`
- **_drop_parsed_quantity_or_error()** (6 connections) — `server/commands/inventory_drop_command.py`
- **_drop_finish_after_persist()** (5 connections) — `server/commands/inventory_drop_command.py`
- **test_emit_inventory_updated_emission_error_is_swallowed()** (5 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **test_emit_inventory_updated_no_connection_manager_is_noop()** (5 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **test_emit_inventory_updated_sends_personal_message()** (5 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **_ConnectionManagerLike** (4 connections) — `server/services/inventory_websocket_events.py`
- **_drop_quantity_bounds_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_quantity_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_drop_slot_index_or_error()** (4 connections) — `server/commands/inventory_drop_command.py`
- **_inventory_rows_after_drop()** (4 connections) — `server/commands/inventory_drop_command.py`
- **.send_personal_message()** (3 connections) — `server/services/inventory_websocket_events.py`
- **_async_attr()** (3 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **Player** (3 connections)
- **UUID** (3 connections)
- **asyncio** (3 connections)
- **.get_equipped_items()** (2 connections) — `server/services/inventory_websocket_events.py`
- **.get_inventory()** (2 connections) — `server/services/inventory_websocket_events.py`
- *... and 25 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (23 shared connections)
- [Community 239](Community_239.md) (6 shared connections)
- [Community 441](Community_441.md) (4 shared connections)
- [Community 246](Community_246.md) (3 shared connections)
- [Community 414](Community_414.md) (2 shared connections)
- [Community 450](Community_450.md) (1 shared connections)
- [Community 811](Community_811.md) (1 shared connections)
- [Community 341](Community_341.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)

## Source Files

- `server/commands/inventory_drop_command.py`
- `server/services/inventory_websocket_events.py`
- `server/tests/unit/services/test_inventory_websocket_events.py`

## Audit Trail

- EXTRACTED: 109 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*