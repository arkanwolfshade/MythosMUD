# server tests unit utils test

> 72 nodes

## Key Concepts

- **CommunicationCommandFactory** (39 connections) — `server/utils/command_factories_communication.py`
- **test_command_factories_communication.py** (30 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
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
- *... and 47 more nodes in this community*

## Relationships

- [mythosvalidationerror](mythosvalidationerror.md) (16 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (10 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (9 shared connections)
- [server models command base basecommand](server_models_command_base_basecommand.md) (3 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [server monitoring exception metrics](server_monitoring_exception_metrics.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 126 (76%)
- INFERRED: 39 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*