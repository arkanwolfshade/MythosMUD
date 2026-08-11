# NPC Occupant Processor

> 88 nodes

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
- *... and 63 more nodes in this community*

## Relationships

- [Zone Config Loader](Zone_Config_Loader.md) (25 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (17 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (9 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (8 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (8 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/tests/unit/models/test_command_communication.py`

## Audit Trail

- EXTRACTED: 278 (89%)
- INFERRED: 34 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*