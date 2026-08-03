# command factories create

> 178 nodes

## Key Concepts

- **BaseCommand** (152 connections) — `server/models/command_base.py`
- **CommandFactory** (83 connections) — `server/utils/command_factories.py`
- **test_command_base.py** (22 connections) — `server/tests/unit/models/test_command_base.py`
- **_build_command_factory()** (6 connections) — `server/utils/command_parser.py`
- **test_base_command_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_command_base.py`
- **.create_npc_command()** (4 connections) — `server/utils/command_factories.py`
- **.create_spawn_command()** (4 connections) — `server/utils/command_factories.py`
- **_build_command_factory_part1()** (4 connections) — `server/utils/command_parser.py`
- **_build_command_factory_part2()** (4 connections) — `server/utils/command_parser.py`
- **test_base_command_instantiation()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_model_config()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_slots()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_direction_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **.create_say_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_local_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_system_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_emote_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_me_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_pose_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_whisper_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_reply_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_channel_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_look_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_go_command()** (3 connections) — `server/utils/command_factories.py`
- *... and 153 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (45 shared connections)
- [command models admin](command_models_admin.md) (11 shared connections)
- [command communication models](command_communication_models.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [command inventory models](command_inventory_models.md) (6 shared connections)
- [command models moderation](command_models_moderation.md) (6 shared connections)
- [command combat models](command_combat_models.md) (5 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (4 shared connections)
- [Spell Validation](Spell_Validation.md) (3 shared connections)
- [command parser rationale](command_parser_rationale.md) (2 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)
- [rescue service services](rescue_service_services.md) (1 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/tests/unit/models/test_command_base.py`
- `server/utils/command_factories.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 524 (87%)
- INFERRED: 77 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*