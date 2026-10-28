# RoomEventHandler

> 31 nodes · cohesion 0.09

## Key Concepts

- **emit_inventory_updated()** (26 connections) — `server/services/inventory_websocket_events.py`
- **test_inventory_websocket_events.py** (9 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **_Owner** (8 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **_InventoryOwner** (6 connections) — `server/services/inventory_websocket_events.py`
- **test_emit_inventory_updated_emission_error_is_swallowed()** (5 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **test_emit_inventory_updated_no_connection_manager_is_noop()** (5 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **test_emit_inventory_updated_sends_personal_message()** (5 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **_ConnectionManagerLike** (4 connections) — `server/services/inventory_websocket_events.py`
- **.send_personal_message()** (3 connections) — `server/services/inventory_websocket_events.py`
- **UUID** (3 connections)
- **_async_attr()** (3 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **asyncio** (3 connections)
- **.get_equipped_items()** (2 connections) — `server/services/inventory_websocket_events.py`
- **.get_inventory()** (2 connections) — `server/services/inventory_websocket_events.py`
- **Protocol** (2 connections)
- **mock_connection_manager()** (2 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **Minimal shape emit_inventory_updated needs from a player.** (1 connections) — `server/services/inventory_websocket_events.py`
- **Return the player's carried inventory stacks.** (1 connections) — `server/services/inventory_websocket_events.py`
- **Return the player's equipped-slot items.** (1 connections) — `server/services/inventory_websocket_events.py`
- **Minimal shape emit_inventory_updated needs from a connection manager.…** (1 connections) — `server/services/inventory_websocket_events.py`
- **Send event to a single player; returns delivery status.** (1 connections) — `server/services/inventory_websocket_events.py`
- **Emit inventory_updated to the player personally. connection_manager is typed as…** (1 connections) — `server/services/inventory_websocket_events.py`
- **.get_equipped_items()** (1 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **.get_inventory()** (1 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- **.__init__()** (1 connections) — `server/tests/unit/services/test_inventory_websocket_events.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (13 shared connections)
- [deprecated_patterns.py](deprecated_patterns.py.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (2 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (2 shared connections)
- [Protocol](Protocol.md) (1 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)

## Source Files

- `server/services/inventory_websocket_events.py`
- `server/tests/unit/services/test_inventory_websocket_events.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*