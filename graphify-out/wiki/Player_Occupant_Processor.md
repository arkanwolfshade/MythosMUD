# Player Occupant Processor

> 34 nodes

## Key Concepts

- **test_look_container_helpers.py** (45 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **_format_container_contents()** (11 connections) — `server/commands/look_container.py`
- **test_format_container_contents_with_quantity()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_via_inner_container_no_inner_container()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_via_inner_container_invalid_uuid()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_via_inner_container_no_get_container()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_matches_item_instance_id_true()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_matches_item_instance_id_false()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_matches_item_instance_id_none()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_matches_name_or_slot_slot_match()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_matches_name_or_slot_name_match()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_matches_name_or_slot_no_match()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_get_container_data_from_component_no_container_id()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_get_container_data_from_component_no_get_container()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_extract_container_metadata_no_metadata()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_format_container_contents_empty()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_format_container_contents_with_quantity()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Format container contents as list of lines.** (1 connections) — `server/commands/look_container.py`
- **Test formatting container contents with quantity > 1.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Unit tests for look container helper functions.  Tests the helper functions in l** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_via_inner_container() when item has no inner_container.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_via_inner_container() with invalid UUID.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_via_inner_container() when persistence has no get_container** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _matches_item_instance_id() returns True when IDs match.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _matches_item_instance_id() returns False when IDs don't match.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- *... and 9 more nodes in this community*

## Relationships

- [Player State Command Factory](Player_State_Command_Factory.md) (20 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (10 shared connections)
- [Health Check Service](Health_Check_Service.md) (8 shared connections)
- [Container System Architecture](Container_System_Architecture.md) (6 shared connections)
- [Look Container Command](Look_Container_Command.md) (4 shared connections)

## Source Files

- `server/commands/look_container.py`
- `server/tests/unit/commands/test_look_container.py`
- `server/tests/unit/commands/test_look_container_helpers.py`

## Audit Trail

- EXTRACTED: 118 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*