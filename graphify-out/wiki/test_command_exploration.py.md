# test_command_exploration.py

> 34 nodes · cohesion 0.07

## Key Concepts

- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **test_go_command_missing_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **test_go_command_all_directions()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_required_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_none()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_instance_number()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_look_in()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **Command for looking around, in a specific direction, or at an NPC.** (1 connections) — `server/models/command_exploration.py`
- **Validate direction is one of the allowed values.** (1 connections) — `server/models/command_exploration.py`
- **Unit tests for exploration command models.  Tests the LookCommand and GoCommand** (1 connections) — `server/tests/unit/models/test_command_exploration.py`
- **Test GoCommand validates valid direction.** (1 connections) — `server/tests/unit/models/test_command_exploration.py`
- **Test GoCommand rejects invalid direction.** (1 connections) — `server/tests/unit/models/test_command_exploration.py`
- **Test GoCommand accepts all valid directions.** (1 connections) — `server/tests/unit/models/test_command_exploration.py`
- **Test GoCommand requires direction (cannot be None).** (1 connections) — `server/tests/unit/models/test_command_exploration.py`
- **Test LookCommand has correct default values.** (1 connections) — `server/tests/unit/models/test_command_exploration.py`
- *... and 9 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (15 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [test_command_factories_exploration.py](test_command_factories_exploration.py.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)

## Source Files

- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 97 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*