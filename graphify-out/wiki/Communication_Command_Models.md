# Communication Command Models

> 86 nodes · cohesion 0.04

## Key Concepts

- **test_command_communication.py** (44 connections) — `server/tests/unit/models/test_command_communication.py`
- **WhisperCommand** (15 connections) — `server/models/command_communication.py`
- **EmoteCommand** (12 connections) — `server/models/command_communication.py`
- **LocalCommand** (12 connections) — `server/models/command_communication.py`
- **MeCommand** (12 connections) — `server/models/command_communication.py`
- **ReplyCommand** (12 connections) — `server/models/command_communication.py`
- **SayCommand** (12 connections) — `server/models/command_communication.py`
- **SystemCommand** (12 connections) — `server/models/command_communication.py`
- **Validate message content for security using centralized validation.** (4 connections) — `server/models/command_communication.py`
- **Test SayCommand validates message min length.** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **.validate_action()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_action()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_message()** (3 connections) — `server/models/command_communication.py`
- **.validate_target()** (3 connections) — `server/models/command_communication.py`
- **Test SayCommand calls validate_message_content.** (3 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_max_length()** (3 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_min_length()** (3 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_validate_action_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_local_command_message_max_length()** (3 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_local_command_message_min_length()** (3 connections) — `server/tests/unit/models/test_command_communication.py`
- *... and 61 more nodes in this community*

## Relationships

- [[Base Command Models]] (34 shared connections)
- [[Command Field Validators]] (15 shared connections)
- [[Communication Command Factories]] (1 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/tests/unit/models/test_command_communication.py`

## Audit Trail

- EXTRACTED: 296 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
