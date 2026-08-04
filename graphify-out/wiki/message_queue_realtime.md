# message queue realtime

> 77 nodes

## Key Concepts

- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_base.py** (22 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **test_base_command_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_command_base.py`
- **test_look_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_missing_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **test_base_command_instantiation()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_model_config()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_slots()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_direction_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_look_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_none()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_look_in()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_instance_number()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_required_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- *... and 52 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (16 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (7 shared connections)
- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [Inventory Equip](Inventory_Equip.md) (3 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (1 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_base.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 205 (89%)
- INFERRED: 25 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*