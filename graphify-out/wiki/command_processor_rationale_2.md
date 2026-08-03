# command processor rationale

> 81 nodes

## Key Concepts

- **test_command_processor.py** (39 connections) — `server/tests/unit/utils/test_command_processor.py`
- **CommandProcessor** (15 connections) — `server/utils/command_processor.py`
- **command_processor.py** (13 connections) — `server/utils/command_processor.py`
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
- *... and 56 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (3 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [look helpers commands](look_helpers_commands.md) (2 shared connections)
- [command parser rationale](command_parser_rationale.md) (2 shared connections)
- [health service services](health_service_services.md) (1 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_processor.py`

## Audit Trail

- EXTRACTED: 199 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*