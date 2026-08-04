# services admin auth

> 42 nodes

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
- **_app_state_container_service()** (4 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ensure_item_instance_for_put()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_strip_cmd_field()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_extract_items_json_branch()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_extract_items_dict_branch()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_inventory_rows_from_transfer_result()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **test_extract_items_from_container_dict()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_extract_items_from_container_items_json_attr()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_parse_json_string_items_valid()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_parse_json_string_items_invalid_returns_none()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_filter_valid_items_drops_non_dict()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_parse_container_items_full_pipeline()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_resolve_container_id_explicit()** (2 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- *... and 17 more nodes in this community*

## Relationships

- [container inventory helpers](container_inventory_helpers.md) (36 shared connections)
- [container find inventory](container_find_inventory.md) (8 shared connections)
- [logout command commands](logout_command_commands.md) (7 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (5 shared connections)
- [container inventory display](container_inventory_display.md) (4 shared connections)
- [commands inventory command](commands_inventory_command.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory.py`
- `server/commands/container_helpers_inventory_ops.py`
- `server/tests/unit/commands/test_container_helpers_inventory_ops.py`

## Audit Trail

- EXTRACTED: 204 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*