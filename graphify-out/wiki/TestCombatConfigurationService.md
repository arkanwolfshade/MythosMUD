# TestCombatConfigurationService

> 42 nodes

## Key Concepts

- **Direction** (28 connections) — `server/models/command_base.py`
- **test_command_exploration.py** (22 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (18 connections) — `server/models/command_exploration.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **command_exploration.py** (10 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (4 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (4 connections) — `server/models/command_exploration.py`
- **test_go_command_all_directions()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_required_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_valid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_valid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_missing_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_invalid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_invalid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_none()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_instance_number()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_look_in()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **StrEnum** (2 connections)
- **field_validator** (2 connections)
- **Validate direction is one of the allowed values.** (2 connections) — `server/models/command_exploration.py`
- **Test LookCommand can be created with a target.** (2 connections) — `server/tests/unit/models/test_command_exploration.py`
- *... and 17 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (18 shared connections)
- [Persistence Layer Refactoring - COMPLETE ✅](Persistence_Layer_Refactoring_-_COMPLETE_✅.md) (5 shared connections)
- [.change_position](change_position.md) (3 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (3 shared connections)
- [sub_zone](sub_zone.md) (1 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 84 (82%)
- INFERRED: 18 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*