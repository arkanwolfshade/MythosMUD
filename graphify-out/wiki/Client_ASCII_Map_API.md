# Client ASCII Map API

> 28 nodes

## Key Concepts

- **_find_container_wearable()** (20 connections) — `server/commands/look_container.py`
- **test_find_container_wearable_success()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_by_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_with_inner_container()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_wearable_found()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_empty()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_no_match()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_multiple_matches()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **test_find_container_wearable_instance_number_out_of_range()** (3 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Find a wearable container in equipped items by name or prototype_id.      This f** (1 connections) — `server/commands/look_container.py`
- **Test finding wearable container by name.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding wearable container by prototype_id.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding wearable container when not found.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding wearable container with inner_container.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding wearable container with instance number.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test finding wearable container with invalid instance number.** (1 connections) — `server/tests/unit/commands/test_look_container.py`
- **Test _find_container_wearable() finds wearable container.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() returns None when container not found.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() with empty dict.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- **Test _find_container_wearable() with no matching containers.** (1 connections) — `server/tests/unit/commands/test_look_container_helpers.py`
- *... and 3 more nodes in this community*

## Relationships

- [Player State Command Factory](Player_State_Command_Factory.md) (8 shared connections)
- [Look Container Command](Look_Container_Command.md) (7 shared connections)
- [Server Process Termination](Server_Process_Termination.md) (4 shared connections)

## Source Files

- `server/commands/look_container.py`
- `server/tests/unit/commands/test_look_container.py`
- `server/tests/unit/commands/test_look_container_helpers.py`

## Audit Trail

- EXTRACTED: 73 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*