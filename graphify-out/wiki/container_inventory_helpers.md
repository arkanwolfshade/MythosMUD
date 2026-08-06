# container inventory helpers

> 83 nodes

## Key Concepts

- **test_container_helpers_inventory_ops.py** (52 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **container_helpers_inventory_ops.py** (29 connections) — `server/commands/container_helpers_inventory_ops.py`
- **transfer_item_to_container()** (20 connections) — `server/commands/container_helpers_inventory_ops.py`
- **transfer_item_from_container()** (18 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_player_with_inventory()** (17 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **UUID** (12 connections)
- **validate_put_command_inputs()** (12 connections) — `server/commands/container_helpers_inventory_ops.py`
- **parse_container_items()** (11 connections) — `server/commands/container_helpers_inventory_ops.py`
- **extract_items_from_container()** (10 connections) — `server/commands/container_helpers_inventory_ops.py`
- **parse_json_string_items()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **resolve_container_id()** (9 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_coerce_transfer_quantity()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_int_transfer_qty()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **Player** (8 connections)
- **filter_valid_items()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **find_item_in_container()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **validate_get_command_inputs()** (8 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ensure_mutation_token()** (6 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_ContainerSvcTokenOnly** (6 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **_app_state_container_service()** (4 connections) — `server/commands/container_helpers_inventory_ops.py`
- **test_transfer_item_to_container_no_transfer_to_method()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_no_transfer_from()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **test_transfer_item_from_container_inventory_rows_fallback_non_dict_result()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_ops.py`
- **_ensure_item_instance_for_put()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_strip_cmd_field()** (3 connections) — `server/commands/container_helpers_inventory_ops.py`
- *... and 58 more nodes in this community*

## Relationships

- [game rationale schemas](game_rationale_schemas.md) (14 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (5 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (3 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)
- [game weapon player](game_weapon_player.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_ops.py`
- `server/tests/unit/commands/test_container_helpers_inventory_ops.py`

## Audit Trail

- EXTRACTED: 381 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*