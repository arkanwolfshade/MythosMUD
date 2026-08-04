# command inventory factories

> 142 nodes

## Key Concepts

- **BaseCommand** (152 connections) — `server/models/command_base.py`
- **CommandFactory** (83 connections) — `server/utils/command_factories.py`
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
- **.create_following_command()** (3 connections) — `server/utils/command_factories.py`
- *... and 117 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (43 shared connections)
- [command communication models](command_communication_models.md) (8 shared connections)
- [message queue realtime](message_queue_realtime.md) (7 shared connections)
- [admin auth service](admin_auth_service.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [commands who helpers](commands_who_helpers.md) (6 shared connections)
- [npc commands admin](npc_commands_admin.md) (6 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (5 shared connections)
- [player presence tracker](player_presence_tracker.md) (3 shared connections)
- [command commands talk](command_commands_talk.md) (2 shared connections)
- [command parser rationale](command_parser_rationale.md) (2 shared connections)
- [factory](factory.md) (1 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/utils/command_factories.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 447 (86%)
- INFERRED: 73 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*