# room service sync

> 38 nodes

## Key Concepts

- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **test_look_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_missing_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
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
- **Command for looking around, in a specific direction, or at an NPC.** (1 connections) — `server/models/command_exploration.py`
- **Validate direction is one of the allowed values.** (1 connections) — `server/models/command_exploration.py`
- **Command for moving in a specific direction.** (1 connections) — `server/models/command_exploration.py`
- **Validate direction is one of the allowed values.** (1 connections) — `server/models/command_exploration.py`
- **Unit tests for exploration command models.  Tests the LookCommand and GoCommand** (1 connections) — `server/tests/unit/models/test_command_exploration.py`
- **Test LookCommand has correct default values.** (1 connections) — `server/tests/unit/models/test_command_exploration.py`
- *... and 13 more nodes in this community*

## Relationships

- [dialogue definition persistence](dialogue_definition_persistence.md) (13 shared connections)
- [add used user](add_used_user.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Inventory Equip](Inventory_Equip.md) (2 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)

## Source Files

- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 113 (91%)
- INFERRED: 11 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*