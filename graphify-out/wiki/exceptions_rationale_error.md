# exceptions rationale error

> 30 nodes

## Key Concepts

- **test_command_factories_utility.py** (51 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **.create_summon_command()** (14 connections) — `server/utils/command_factories_utility.py`
- **test_create_summon_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_invalid_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_negative_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_invalid_token()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_extra_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_invalid_direction()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_with_quantity()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_with_target_type()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_with_quantity_and_type()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_with_direction()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Unit tests for utility command factories.  Tests the UtilityCommandFactory class** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() creates SummonCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() with quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() with target type.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() with quantity and target type.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() raises error with invalid quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() raises error with negative quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() raises error with invalid token.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_summon_command() raises error with extra args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- *... and 5 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [event events serialization](event_events_serialization.md) (7 shared connections)
- [command models admin](command_models_admin.md) (5 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (4 shared connections)
- [config models game](config_models_game.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (3 shared connections)
- [services service hallucination](services_service_hallucination.md) (3 shared connections)
- [message handler factory](message_handler_factory.md) (3 shared connections)
- [casting game magic](casting_game_magic.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [message realtime messaging](message_realtime_messaging.md) (2 shared connections)
- [countdown rest task](countdown_rest_task.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 118 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*