# rescue service services

> 70 nodes

## Key Concepts

- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **CommunicationCommandFactory** (15 connections) — `server/utils/command_factories_communication.py`
- **.create_local_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_say_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_system_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_emote_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_me_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_pose_command()** (5 connections) — `server/utils/command_factories_communication.py`
- **test_create_say_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_local_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_no_message()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_reply_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_local_command_too_long()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_system_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_emote_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_me_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_channel_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_channel_command_default_no_channel()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_reply_command_empty_message()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_too_long()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_say_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- *... and 45 more nodes in this community*

## Relationships

- [command inventory models](command_inventory_models.md) (14 shared connections)
- [spell game magic](spell_game_magic.md) (11 shared connections)
- [command communication models](command_communication_models.md) (8 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (1 shared connections)
- [command processor rationale](command_processor_rationale.md) (1 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 209 (93%)
- INFERRED: 15 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*