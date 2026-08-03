# command models admin

> 163 nodes

## Key Concepts

- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **.create_look_command()** (18 connections) — `server/utils/command_factories_exploration.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **NPCCommand** (13 connections) — `server/models/command_admin.py`
- **GotoCommand** (13 connections) — `server/models/command_admin.py`
- **ShutdownCommand** (12 connections) — `server/models/command_admin.py`
- **.create_teleport_command()** (11 connections) — `server/utils/command_factories_utility.py`
- **command_exploration.py** (9 connections) — `server/models/command_exploration.py`
- **test_npc_command_subcommand_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_subcommand_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_validate_prototype_id_invalid_characters()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_validation_max()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_player_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_player_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_player_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- *... and 138 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (33 shared connections)
- [command utility models](command_utility_models.md) (25 shared connections)
- [command factories create](command_factories_create.md) (11 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (5 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (4 shared connections)
- [countdown rest task](countdown_rest_task.md) (1 shared connections)
- [message realtime messaging](message_realtime_messaging.md) (1 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (1 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [npc services combat](npc_services_combat.md) (1 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_admin.py`
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/utils/test_command_factories_exploration.py`
- `server/utils/command_factories_exploration.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 494 (91%)
- INFERRED: 51 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*