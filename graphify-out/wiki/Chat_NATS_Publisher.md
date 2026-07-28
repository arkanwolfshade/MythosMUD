# Chat NATS Publisher

> 17 nodes · cohesion 0.13

## Key Concepts

- **chat_nats_publisher.py** (29 connections) — `server/game/chat_nats_publisher.py`
- **_build_standardized_subject()** (9 connections) — `server/game/chat_nats_publisher.py`
- **chat_validator.py** (9 connections) — `server/game/chat_validator.py`
- **Any** (8 connections)
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_extract_subzone_from_room()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **validate_chat_message()** (5 connections) — `server/game/chat_validator.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **validate_room_access()** (4 connections) — `server/game/chat_validator.py`
- **contains_malicious_content()** (3 connections) — `server/game/chat_validator.py`
- **Chat NATS publishing utilities.  This module provides NATS subject building and** (1 connections) — `server/game/chat_nats_publisher.py`
- **Chat message validation utilities.  This module provides validation functions fo** (1 connections) — `server/game/chat_validator.py`
- **Validate chat message before transmission.      Args:         chat_message: The** (1 connections) — `server/game/chat_validator.py`
- **Validate sender has access to the room.      Args:         sender_id: ID of the** (1 connections) — `server/game/chat_validator.py`
- **Check for malicious content patterns.      Args:         content: The message co** (1 connections) — `server/game/chat_validator.py`

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (9 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (6 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Admin Set Stat Command](Admin_Set_Stat_Command.md) (2 shared connections)
- [Logging Migration Complete](Logging_Migration_Complete.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/game/chat_validator.py`

## Audit Trail

- EXTRACTED: 95 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*