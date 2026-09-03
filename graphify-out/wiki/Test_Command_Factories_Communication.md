# Test Command Factories Communication

> 68 nodes

## Key Concepts

- **CommunicationCommandFactory** (39 connections) — `server/utils/command_factories_communication.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_local_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_emote_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_me_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_say_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_system_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **test_create_channel_command_default_no_channel()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_channel_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_emote_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_local_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_local_command_too_long()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_me_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_reply_command_empty_message()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_reply_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_say_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_system_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_no_message()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_whisper_command_too_long()** (5 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **.create_pose_command()** (5 connections) — `server/utils/command_factories_communication.py`
- **test_create_channel_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_create_channel_command_with_default()** (4 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- *... and 43 more nodes in this community*

## Relationships

- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (26 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (14 shared connections)
- [Command Aliases](Command_Aliases.md) (9 shared connections)
- [Test Command Factories Utility](Test_Command_Factories_Utility.md) (8 shared connections)
- [Test Command Factories Player State](Test_Command_Factories_Player_State.md) (1 shared connections)
- [Command Factories](Command_Factories.md) (1 shared connections)
- [Pydantic Error Handler](Pydantic_Error_Handler.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 112 (74%)
- INFERRED: 39 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*