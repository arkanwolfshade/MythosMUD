# app tick game

> 25 nodes

## Key Concepts

- **test_chat_validator.py** (21 connections) — `server/tests/unit/game/test_chat_validator.py`
- **validate_chat_message()** (12 connections) — `server/game/chat_validator.py`
- **chat_validator.py** (10 connections) — `server/game/chat_validator.py`
- **validate_room_access()** (9 connections) — `server/game/chat_validator.py`
- **_message()** (8 connections) — `server/tests/unit/game/test_chat_validator.py`
- **contains_malicious_content()** (7 connections) — `server/game/chat_validator.py`
- **test_validate_chat_message_accepts_valid_message()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_rejects_empty_content()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_rejects_too_long_content()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_rejects_missing_sender()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_rejects_malicious_script()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_chat_message_handles_invalid_object()** (3 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_room_access_allows_none_room_for_system()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_room_access_rejects_empty_sender()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_room_access_rejects_blank_room_id()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_validate_room_access_accepts_valid_room()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_contains_malicious_content_detects_patterns()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_contains_malicious_content_allows_safe_text()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **test_contains_malicious_content_fails_safe_on_type_error()** (2 connections) — `server/tests/unit/game/test_chat_validator.py`
- **Chat message validation utilities.  This module provides validation functions fo** (1 connections) — `server/game/chat_validator.py`
- **Validate chat message before transmission.      Args:         chat_message: The** (1 connections) — `server/game/chat_validator.py`
- **Validate sender has access to the room.      Args:         sender_id: ID of the** (1 connections) — `server/game/chat_validator.py`
- **Check for malicious content patterns.      Args:         content: The message co** (1 connections) — `server/game/chat_validator.py`
- **ChatMessage** (1 connections)
- **Unit tests for chat message validation helpers.** (1 connections) — `server/tests/unit/game/test_chat_validator.py`

## Relationships

- [chat game message](chat_game_message.md) (5 shared connections)
- [alias command models](alias_command_models.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)

## Source Files

- `server/game/chat_validator.py`
- `server/tests/unit/game/test_chat_validator.py`

## Audit Trail

- EXTRACTED: 104 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*