# Invite and User Schemas

> 60 nodes

## Key Concepts

- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **.create_look_command()** (18 connections) — `server/utils/command_factories_exploration.py`
- **test_look_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
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
- **test_create_look_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_target()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_explicit_player_type()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_explicit_npc_type()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_explicit_item_type()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_explicit_container_type()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_explicit_type_no_target()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_instance_hyphen()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_look_command_with_instance_space()** (3 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- *... and 35 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (16 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (13 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (4 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (1 shared connections)

## Source Files

- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/utils/test_command_factories_exploration.py`
- `server/utils/command_factories_exploration.py`

## Audit Trail

- EXTRACTED: 163 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*