# command factories create

> 144 nodes

## Key Concepts

- **BaseCommand** (152 connections) — `server/models/command_base.py`
- **CommandFactory** (83 connections) — `server/utils/command_factories.py`
- **command_parser.py** (46 connections) — `server/utils/command_parser.py`
- **_build_command_factory()** (6 connections) — `server/utils/command_parser.py`
- **.create_npc_command()** (4 connections) — `server/utils/command_factories.py`
- **.create_spawn_command()** (4 connections) — `server/utils/command_factories.py`
- **_build_command_factory_part1()** (4 connections) — `server/utils/command_parser.py`
- **_build_command_factory_part2()** (4 connections) — `server/utils/command_parser.py`
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
- **.create_sit_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_stand_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_lie_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_ground_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_follow_command()** (3 connections) — `server/utils/command_factories.py`
- **.create_unfollow_command()** (3 connections) — `server/utils/command_factories.py`
- *... and 119 more nodes in this community*

## Relationships

- [container persistence rationale](container_persistence_rationale.md) (32 shared connections)
- [command communication models](command_communication_models.md) (9 shared connections)
- [calendar schemas validate](calendar_schemas_validate.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [npc commands admin](npc_commands_admin.md) (6 shared connections)
- [command models moderation](command_models_moderation.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (6 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (5 shared connections)
- [combat attack handler](combat_attack_handler.md) (5 shared connections)
- [room sync service](room_sync_service.md) (5 shared connections)
- [feature services flag](feature_services_flag.md) (4 shared connections)
- [commands who helpers](commands_who_helpers.md) (4 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/utils/command_factories.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 494 (87%)
- INFERRED: 73 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*