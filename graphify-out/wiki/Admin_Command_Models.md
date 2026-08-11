# Admin Command Models

> 32 nodes

## Key Concepts

- **_find_container_in_room()** (22 connections) — `server/commands/look_container.py`
- **test_find_container_in_room_success()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_by_container_id()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_found()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_in_room_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_in_room_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_in_room_empty()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_in_room_no_match()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_in_room_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_in_room_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_in_room_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_in_room_instance_number_zero()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Find a container in room containers by name or container_id.      Args:** (1 connections) — `server/commands/look_container.py`
- **Test finding container in room by name.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding container in room by container_id.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding container in room when not found.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding container in room with multiple matches.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding container in room with instance number.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding container in room with invalid instance number.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test _find_container_in_room() finds container by name.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_in_room() returns None when container not found.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- *... and 7 more nodes in this community*

## Relationships

- [Player Occupant Processor](Player_Occupant_Processor.md) (10 shared connections)
- [Look Container Command](Look_Container_Command.md) (7 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (4 shared connections)

## Source Files

- `server/commands/look_container.py`
- `server/tests/unit/commands/test_look_container.py`
- `server/tests/unit/commands/test_look_container_helpers.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*