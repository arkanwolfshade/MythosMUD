# server tests unit utils test

> 70 nodes

## Key Concepts

- **CommunicationCommandFactory** (39 connections) — `server/utils/command_factories_communication.py`
- **test_command_factories_communication.py** (30 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
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
- *... and 45 more nodes in this community*

## Relationships

- [server exceptions rationale 179](server_exceptions_rationale_179.md) (14 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [server models command](server_models_command.md) (9 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (2 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 117 (75%)
- INFERRED: 39 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*