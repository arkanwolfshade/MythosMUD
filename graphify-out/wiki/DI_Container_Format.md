# DI Container Format

> 50 nodes

## Key Concepts

- **test_look_container.py** (55 connections) — `server/tests/unit/commands/test_look_container.py`
- **_get_container_description()** (10 connections) — `server/commands/look_container.py`
- **test_get_container_description_from_item()** (4 connections) — `server/tests/unit/commands/test_look_container.py`
- **sample_container()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_via_inner_container()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_via_inner_container_no_inner_container()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_via_inner_container_invalid_uuid()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_format_container_contents_with_items()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_format_container_contents_empty()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_get_container_description_from_container_metadata()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_get_container_description_no_registry()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_get_container_description_no_prototype_id()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_or_equipped_in_room()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_or_equipped_in_equipped()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_or_equipped_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_handle_container_look_success()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_handle_container_look_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_try_lookup_container_implicit_success()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_try_lookup_container_implicit_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_get_container_description_prototype_error()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_via_inner_container_no_get_container_method()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_or_equipped_no_get_containers()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_find_container_in_room_or_equipped_no_get_equipped_items()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **sample_equipped_container()** (2 connections) — `server/tests/unit/commands/test_look_container.py`
- **mock_prototype_registry()** (2 connections) — `server/tests/unit/commands/test_look_container.py`
- *... and 25 more nodes in this community*

## Relationships

- [startup npc services](startup_npc_services.md) (21 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (9 shared connections)
- [command processor rationale](command_processor_rationale.md) (7 shared connections)
- [status game spell](status_game_spell.md) (7 shared connections)
- [schemas validator rationale](schemas_validator_rationale.md) (4 shared connections)

## Source Files

- `server/commands/look_container.py`
- `server/tests/unit/commands/test_look_container.py`

## Audit Trail

- EXTRACTED: 156 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*