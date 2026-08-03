# taunt combat commands

> 73 nodes

## Key Concepts

- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **.create_look_command()** (18 connections) — `server/utils/command_factories_exploration.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **test_look_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_missing_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **test_direction_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_look_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_none()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_look_in()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_instance_number()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_required_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_all_directions()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_create_look_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_target()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_explicit_player_type()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- *... and 48 more nodes in this community*

## Relationships

- [Inventory Equip](Inventory_Equip.md) (16 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (13 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (7 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [room sync service](room_sync_service.md) (2 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (1 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_base.py`
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/utils/test_command_factories_exploration.py`
- `server/utils/command_factories_exploration.py`

## Audit Trail

- EXTRACTED: 205 (90%)
- INFERRED: 23 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*