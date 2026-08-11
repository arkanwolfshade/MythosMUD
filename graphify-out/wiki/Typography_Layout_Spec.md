# Typography Layout Spec

> 25 nodes

## Key Concepts

- **chat_nats_publisher.py** (21 connections) — `server/game/chat_nats_publisher.py`
- **publish_chat_message_to_nats()** (16 connections) — `server/game/chat_nats_publisher.py`
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **chat_validator.py** (8 connections) — `server/game/chat_validator.py`
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_extract_subzone_from_room()** (5 connections) — `server/game/chat_nats_publisher.py`
- **Any** (5 connections)
- **validate_chat_message()** (5 connections) — `server/game/chat_validator.py`
- **_subject_whisper_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **validate_room_access()** (4 connections) — `server/game/chat_validator.py`
- **contains_malicious_content()** (3 connections) — `server/game/chat_validator.py`
- **Chat NATS publishing utilities.  This module provides NATS subject building and** (1 connections) — `server/game/chat_nats_publisher.py`
- **Extract subzone from room_id, returning 'unknown' if extraction fails.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build whisper subject; returns fallback 'chat.whisper' if no target_id.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build party subject; returns None if no party_id.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build NATS subject using standardized patterns via subject_manager.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build NATS subject using legacy construction (backward compatibility).** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build NATS subject using standardized patterns or fallback to legacy constructio** (1 connections) — `server/game/chat_nats_publisher.py`
- **Publish a chat message to NATS for real-time distribution.      This function pu** (1 connections) — `server/game/chat_nats_publisher.py`
- **Chat message validation utilities.  This module provides validation functions fo** (1 connections) — `server/game/chat_validator.py`
- **Validate chat message before transmission.      Args:         chat_message: The** (1 connections) — `server/game/chat_validator.py`
- **Validate sender has access to the room.      Args:         sender_id: ID of the** (1 connections) — `server/game/chat_validator.py`
- **Check for malicious content patterns.      Args:         content: The message co** (1 connections) — `server/game/chat_validator.py`

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (10 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (2 shared connections)
- [Cursor Setup Guide](Cursor_Setup_Guide.md) (2 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/game/chat_validator.py`

## Audit Trail

- EXTRACTED: 104 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*