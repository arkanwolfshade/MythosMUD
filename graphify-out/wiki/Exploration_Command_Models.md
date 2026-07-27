# Exploration Command Models

> 41 nodes · cohesion 0.08

## Key Concepts

- **Direction** (18 connections) — `server/models/command_base.py`
- **LookCommand** (18 connections) — `server/models/command_exploration.py`
- **test_command_exploration.py** (18 connections) — `server/tests/unit/models/test_command_exploration.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **command_exploration.py** (8 connections) — `server/models/command_exploration.py`
- **Direction** (5 connections) — `server/models/command_exploration.py`
- **Direction** (4 connections) — `server/models/command_admin.py`
- **.validate_direction_field()** (3 connections) — `server/models/command_admin.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **test_go_command_all_directions()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_missing_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_required_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_invalid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_invalid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_none()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_instance_number()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_look_in()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **Validate direction is one of the allowed values.** (2 connections) — `server/models/command_exploration.py`
- *... and 16 more nodes in this community*

## Relationships

- [[Base Command Models]] (21 shared connections)
- [[Admin Command Models]] (7 shared connections)
- [[Spell Registry Costs]] (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 136 (87%)
- INFERRED: 21 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
