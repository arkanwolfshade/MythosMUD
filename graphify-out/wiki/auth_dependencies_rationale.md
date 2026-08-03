# auth dependencies rationale

> 10 nodes

## Key Concepts

- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **.create_spells_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **test_create_spells_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **._resolve_heal_cast()** (4 connections) — `server/utils/command_factories_utility.py`
- **test_create_spells_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_spells_command() creates SpellsCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Test create_spells_command() raises error with args.** (1 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **Factory class for creating utility command objects.** (1 connections) — `server/utils/command_factories_utility.py`
- **Resolve 'heal' command variations to (spell_name, target). Returns None if not a** (1 connections) — `server/utils/command_factories_utility.py`
- **Create SpellsCommand from arguments.** (1 connections) — `server/utils/command_factories_utility.py`

## Relationships

- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (4 shared connections)
- [event events serialization](event_events_serialization.md) (2 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)
- [config models game](config_models_game.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)
- [message realtime messaging](message_realtime_messaging.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [services service hallucination](services_service_hallucination.md) (1 shared connections)
- [countdown rest task](countdown_rest_task.md) (1 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (1 shared connections)
- [message handler factory](message_handler_factory.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 40 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*