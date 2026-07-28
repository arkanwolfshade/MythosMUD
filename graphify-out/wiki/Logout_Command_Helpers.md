# Logout Command Helpers

> 155 nodes · cohesion 0.02

## Key Concepts

- **test_look_container.py** (55 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_look_container_helpers.py** (45 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **look_container.py** (23 connections) — `server/commands/look_container.py`
- **_find_container_wearable()** (20 connections) — `server/commands/look_container.py`
- **_format_container_display()** (19 connections) — `server/commands/look_container.py`
- **_find_container_in_room_or_equipped()** (14 connections) — `server/commands/look_container.py`
- **Any** (14 connections)
- **_find_container_via_inner_container()** (13 connections) — `server/commands/look_container.py`
- **_format_container_contents()** (11 connections) — `server/commands/look_container.py`
- **_handle_container_look()** (11 connections) — `server/commands/look_container.py`
- **_get_container_description()** (10 connections) — `server/commands/look_container.py`
- **_matches_item_instance_id()** (8 connections) — `server/commands/look_container.py`
- **_try_match_container_component()** (8 connections) — `server/commands/look_container.py`
- **_get_container_data_from_component()** (7 connections) — `server/commands/look_container.py`
- **_matches_name_or_slot()** (7 connections) — `server/commands/look_container.py`
- **_extract_container_metadata()** (6 connections) — `server/commands/look_container.py`
- **_find_container_via_wearable_service()** (6 connections) — `server/commands/look_container.py`
- **test_get_container_description_from_item()** (4 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_extract_container_metadata_no_metadata()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_via_inner_container_invalid_uuid()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_via_inner_container_no_get_container()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_via_inner_container_no_inner_container()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_empty()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_found()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- *... and 130 more nodes in this community*

## Relationships

- [Client Architecture Planning](Client_Architecture_Planning.md) (20 shared connections)
- [Async Persistence Core](Async_Persistence_Core.md) (10 shared connections)
- [Look Display Helpers](Look_Display_Helpers.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)

## Source Files

- `server/commands/look_container.py`
- `server/tests/unit/commands/test_look_container.py`
- `server/tests/unit/commands/test_look_container_helpers.py`

## Audit Trail

- EXTRACTED: 534 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*