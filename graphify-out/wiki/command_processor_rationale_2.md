# command processor rationale

> 79 nodes

## Key Concepts

- **test_command_processor.py** (39 connections) — `server/tests/unit/utils/test_command_processor.py`
- **CommandProcessor** (15 connections) — `server/utils/command_processor.py`
- **get_command_processor()** (7 connections) — `server/utils/command_processor.py`
- **.extract_command_data()** (5 connections) — `server/utils/command_processor.py`
- **command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_get_command_processor()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.process_command_string()** (4 connections) — `server/utils/command_processor.py`
- **._extract_attributes()** (4 connections) — `server/utils/command_processor.py`
- **._is_combat_command()** (4 connections) — `server/utils/command_processor.py`
- **test_process_command_string_pydantic_validation_error()** (3 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.__init__()** (3 connections) — `server/utils/command_processor.py`
- **Any** (3 connections)
- **test_command_processor_initialization()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_success()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_value_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_type_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_key_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_command_string_runtime_error()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_attributes_basic()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_extract_attributes_missing_attribute()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_attack()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_punch()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_kick()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_strike()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_is_combat_command_non_combat()** (2 connections) — `server/tests/unit/utils/test_command_processor.py`
- *... and 54 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (6 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (2 shared connections)
- [room sync service](room_sync_service.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [add used user](add_used_user.md) (1 shared connections)
- [payload realtime optimizer](payload_realtime_optimizer.md) (1 shared connections)
- [combat attack handler](combat_attack_handler.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 185 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*