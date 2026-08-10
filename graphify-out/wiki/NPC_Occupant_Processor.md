# NPC Occupant Processor

> 102 nodes

## Key Concepts

- **test_command_communication.py** (45 connections) — `server/tests/unit/models/test_command_communication.py`
- **command_communication.py** (19 connections) — `server/models/command_communication.py`
- **WhisperCommand** (15 connections) — `server/models/command_communication.py`
- **SayCommand** (13 connections) — `server/models/command_communication.py`
- **PoseCommand** (13 connections) — `server/models/command_communication.py`
- **LocalCommand** (12 connections) — `server/models/command_communication.py`
- **SystemCommand** (12 connections) — `server/models/command_communication.py`
- **EmoteCommand** (12 connections) — `server/models/command_communication.py`
- **ReplyCommand** (12 connections) — `server/models/command_communication.py`
- **.create_pose_command()** (5 connections) — `server/utils/command_factories_communication.py`
- **test_say_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_say_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_local_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_local_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_system_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_system_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_pose_command_pose_empty_string()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_pose_command_pose_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_whisper_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_whisper_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_whisper_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_reply_command_message_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_reply_command_message_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- *... and 77 more nodes in this community*

## Relationships

- [Room Service Tests](Room_Service_Tests.md) (30 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (13 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (8 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/tests/unit/models/test_command_communication.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 317 (91%)
- INFERRED: 30 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*