# inventory_item_matching.py

> 111 nodes · cohesion 0.05

## Key Concepts

- **test_container_helpers_inventory_ops.py** (62 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **object** (55 connections)
- **container_helpers_inventory_ops.py** (33 connections) — `server/commands/container_helpers_inventory_ops.py`
- **container_helpers_inventory.py** (32 connections) — `server/commands/container_helpers_inventory.py`
- **transfer_item_to_container()** (24 connections) — `server/commands/container_helpers_inventory_ops.py`
- **asyncio** (22 connections)
- **transfer_item_from_container()** (21 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_player_with_inventory()** (20 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **validate_put_command_inputs()** (14 connections) — `server/commands/container_helpers_inventory_ops.py`
- **parse_container_items()** (13 connections) — `server/commands/container_helpers_inventory_ops.py`
- **UUID** (13 connections)
- **extract_items_from_container()** (11 connections) — `server/commands/container_helpers_inventory_ops.py`
- **validate_get_command_inputs()** (10 connections) — `server/commands/container_helpers_inventory_ops.py`
- **find_item_in_container()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **parse_json_string_items()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **resolve_container_id()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_coerce_transfer_quantity()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **filter_valid_items()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_int_transfer_qty()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **Player** (8 connections)
- **_resolve_container_service()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **patch** (7 connections)
- **test_transfer_item_from_container_inventory_rows_fallback_non_dict_result()** (7 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **_ensure_mutation_token()** (6 connections) — `server/commands/container_helpers_inventory_ops.py`
- **.__init__()** (6 connections) — `server/models/lucidity.py`
- *... and 86 more nodes in this community*

## Relationships

- [SuccessLevel](SuccessLevel.md) (16 shared connections)
- [deprecated_patterns.py](deprecated_patterns.py.md) (7 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (6 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (5 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (4 shared connections)
- [_parse_npc_stats_dict](_parse_npc_stats_dict.md) (4 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (4 shared connections)
- [test_look_player.py](test_look_player.py.md) (4 shared connections)
- [command_parser.py](command_parser.py.md) (4 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (3 shared connections)
- [look_container.py](look_container.py.md) (3 shared connections)
- [Prometheus Configuration](Prometheus_Configuration.md) (2 shared connections)

## Source Files

- `server/commands/container_helpers_inventory.py`
- `server/commands/container_helpers_inventory_ops.py`
- `server/models/lucidity.py`
- `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`

## Audit Trail

- EXTRACTED: 302 (81%)
- INFERRED: 72 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*