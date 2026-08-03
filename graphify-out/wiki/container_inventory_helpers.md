# container inventory helpers

> 44 nodes

## Key Concepts

- **container_helpers_inventory.py** (31 connections) — `server/commands/container_helpers_inventory.py`
- **container_helpers_inventory_ops.py** (29 connections) — `server/commands/container_helpers_inventory_ops.py`
- **UUID** (12 connections)
- **validate_put_command_inputs()** (12 connections) — `server/commands/container_helpers_inventory_ops.py`
- **parse_container_items()** (11 connections) — `server/commands/container_helpers_inventory_ops.py`
- **extract_items_from_container()** (10 connections) — `server/commands/container_helpers_inventory_ops.py`
- **parse_json_string_items()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **resolve_container_id()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **Player** (8 connections)
- **filter_valid_items()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **find_item_in_container()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **validate_get_command_inputs()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ensure_mutation_token()** (6 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_app_state_container_service()** (4 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ensure_item_instance_for_put()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_strip_cmd_field()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_extract_items_json_branch()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_extract_items_dict_branch()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_inventory_rows_from_transfer_result()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **test_extract_items_from_container_items_json_attr()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_validate_get_command_inputs_room_keyword()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_extract_items_from_container_dict()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_parse_json_string_items_valid()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_parse_json_string_items_invalid_returns_none()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_filter_valid_items_drops_non_dict()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- *... and 19 more nodes in this community*

## Relationships

- [npc database infrastructure](npc_database_infrastructure.md) (36 shared connections)
- [inventory commands command](inventory_commands_command.md) (10 shared connections)
- [container find inventory](container_find_inventory.md) (7 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (6 shared connections)
- [container inventory display](container_inventory_display.md) (4 shared connections)
- [combat npc services](combat_npc_services.md) (2 shared connections)
- [commands communication flows](commands_communication_flows.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory.py`
- `server/commands/container_helpers_inventory_ops.py`
- `server/tests/unit/commands/test_container_helpers_inventory_ops.py`

## Audit Trail

- EXTRACTED: 210 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*