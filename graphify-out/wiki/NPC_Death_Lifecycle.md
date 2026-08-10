# NPC Death Lifecycle

> 140 nodes

## Key Concepts

- **BaseCommand** (150 connections) — `server/models/command_base.py`
- **CommandFactory** (82 connections) — `server/utils/command_factories.py`
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
- *... and 115 more nodes in this community*

## Relationships

- [Emote Schema Validator](Emote_Schema_Validator.md) (10 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (8 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (8 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (7 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (6 shared connections)
- [Environmental Container Scenario](Environmental_Container_Scenario.md) (6 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (6 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (6 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (5 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (5 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (5 shared connections)
- [NATS Subject Metrics](NATS_Subject_Metrics.md) (5 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/utils/command_factories.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 441 (86%)
- INFERRED: 72 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*