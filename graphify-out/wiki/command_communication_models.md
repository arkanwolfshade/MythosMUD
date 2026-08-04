# command communication models

> 100 nodes

## Key Concepts

- **test_command_communication.py** (45 connections) — `server/tests/unit/models/test_command_communication.py`
- **WhisperCommand** (15 connections) — `server/models/command_communication.py`
- **SayCommand** (13 connections) — `server/models/command_communication.py`
- **PoseCommand** (13 connections) — `server/models/command_communication.py`
- **LocalCommand** (12 connections) — `server/models/command_communication.py`
- **SystemCommand** (12 connections) — `server/models/command_communication.py`
- **EmoteCommand** (12 connections) — `server/models/command_communication.py`
- **MeCommand** (12 connections) — `server/models/command_communication.py`
- **ReplyCommand** (12 connections) — `server/models/command_communication.py`
- **test_say_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_say_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_local_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_local_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_system_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_system_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_me_command_action_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_me_command_action_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_pose_command_pose_empty_string()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_pose_command_pose_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_whisper_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_whisper_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_whisper_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_reply_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- *... and 75 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (25 shared connections)
- [Loot Generation](Loot_Generation.md) (17 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (8 shared connections)
- [services chat logger](services_chat_logger.md) (8 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/tests/unit/models/test_command_communication.py`

## Audit Trail

- EXTRACTED: 302 (90%)
- INFERRED: 34 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*