# E 2 E Timeout Analysis

> 8 nodes

## Key Concepts

- **chat_validator.py** (8 connections) — `server/game/chat_validator.py`
- **validate_chat_message()** (5 connections) — `server/game/chat_validator.py`
- **validate_room_access()** (4 connections) — `server/game/chat_validator.py`
- **contains_malicious_content()** (3 connections) — `server/game/chat_validator.py`
- **Chat message validation utilities.  This module provides validation functions fo** (1 connections) — `server/game/chat_validator.py`
- **Validate chat message before transmission.      Args:         chat_message: The** (1 connections) — `server/game/chat_validator.py`
- **Validate sender has access to the room.      Args:         sender_id: ID of the** (1 connections) — `server/game/chat_validator.py`
- **Check for malicious content patterns.      Args:         content: The message co** (1 connections) — `server/game/chat_validator.py`

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (2 shared connections)

## Source Files

- `server/game/chat_validator.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*