# Communication Command Classes

> 53 nodes · cohesion 0.04

## Key Concepts

- **command_factories.py** (19 connections) — `server/utils/command_factories.py`
- **CommunicationCommandFactory** (16 connections) — `server/utils/command_factories_communication.py`
- **CombatCommandFactory** (13 connections) — `server/utils/command_factories_combat.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **command_factories_combat.py** (6 connections) — `server/utils/command_factories_combat.py`
- **.create_channel_command()** (4 connections) — `server/utils/command_factories_communication.py`
- **.create_emote_command()** (4 connections) — `server/utils/command_factories_communication.py`
- **.create_local_command()** (4 connections) — `server/utils/command_factories_communication.py`
- **.create_me_command()** (4 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (4 connections) — `server/utils/command_factories_communication.py`
- **.create_say_command()** (4 connections) — `server/utils/command_factories_communication.py`
- **.create_system_command()** (4 connections) — `server/utils/command_factories_communication.py`
- **.create_whisper_command()** (4 connections) — `server/utils/command_factories_communication.py`
- **.create_attack_command()** (3 connections) — `server/utils/command_factories_combat.py`
- **.create_flee_command()** (3 connections) — `server/utils/command_factories_combat.py`
- **.create_kick_command()** (3 connections) — `server/utils/command_factories_combat.py`
- **.create_punch_command()** (3 connections) — `server/utils/command_factories_combat.py`
- **.create_strike_command()** (3 connections) — `server/utils/command_factories_combat.py`
- **.create_taunt_command()** (3 connections) — `server/utils/command_factories_combat.py`
- **.create_pose_command()** (3 connections) — `server/utils/command_factories_communication.py`
- **Factory class for creating combat command objects.** (2 connections) — `server/utils/command_factories_combat.py`
- **Create a ReplyCommand from parsed arguments.** (2 connections) — `server/utils/command_factories_communication.py`
- **AttackCommand** (1 connections) — `server/utils/command_factories_combat.py`
- **ChannelCommand** (1 connections) — `server/utils/command_factories_communication.py`
- **EmoteCommand** (1 connections) — `server/utils/command_factories_communication.py`
- *... and 28 more nodes in this community*

## Relationships

- [[NPC Admin API]] (17 shared connections)
- [[Command Factory Creators]] (6 shared connections)
- [[Base Command Models]] (3 shared connections)
- [[Exploration Command Factory]] (2 shared connections)
- [[Command Factories Inventory]] (2 shared connections)
- [[Command Factories Moderation]] (2 shared connections)
- [[Player State Command Factory]] (2 shared connections)
- [[Admin Command Models]] (2 shared connections)
- [[Alias Expansion Logic]] (1 shared connections)
- [[Command Factories Combat]] (1 shared connections)
- [[Communication Command Factories]] (1 shared connections)

## Source Files

- `server/utils/command_factories.py`
- `server/utils/command_factories_combat.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 147 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
