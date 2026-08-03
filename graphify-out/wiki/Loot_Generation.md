# Loot Generation

> 146 nodes

## Key Concepts

- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **CommunicationCommandFactory** (15 connections) — `server/utils/command_factories_communication.py`
- **ModerationCommandFactory** (13 connections) — `server/utils/command_factories_moderation.py`
- **CombatCommandFactory** (12 connections) — `server/utils/command_factories_combat.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **.create_mute_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_mute_global_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_local_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_unmute_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_global_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_add_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_say_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_system_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_emote_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_me_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_mutes_command()** (6 connections) — `server/utils/command_factories_moderation.py`
- **.create_pose_command()** (5 connections) — `server/utils/command_factories_communication.py`
- *... and 121 more nodes in this community*

## Relationships

- [command inventory models](command_inventory_models.md) (31 shared connections)
- [command inventory factories](command_inventory_factories.md) (24 shared connections)
- [command factories create](command_factories_create.md) (8 shared connections)
- [command communication models](command_communication_models.md) (8 shared connections)
- [services admin auth](services_admin_auth.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [command models moderation](command_models_moderation.md) (6 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (5 shared connections)
- [Inventory Equip](Inventory_Equip.md) (3 shared connections)
- [game chat service](game_chat_service.md) (3 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_combat.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_moderation.py`

## Audit Trail

- EXTRACTED: 474 (95%)
- INFERRED: 27 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*