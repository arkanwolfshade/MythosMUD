# . init ()

> 36 nodes

## Key Concepts

- **chat_nats_publisher.py** (29 connections) — `server/game/chat_nats_publisher.py`
- **_build_standardized_subject()** (9 connections) — `server/game/chat_nats_publisher.py`
- **chat_validator.py** (9 connections) — `server/game/chat_validator.py`
- **Any** (8 connections)
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_extract_subzone_from_room()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_chat_passes_nats_validation()** (5 connections) — `server/game/chat_nats_publisher.py`
- **validate_chat_message()** (5 connections) — `server/game/chat_validator.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_nats_service_ready()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_unexpected_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **validate_room_access()** (4 connections) — `server/game/chat_validator.py`
- **contains_malicious_content()** (3 connections) — `server/game/chat_validator.py`
- **Exception** (1 connections)
- **Chat NATS publishing utilities.  This module provides NATS subject building and** (1 connections) — `server/game/chat_nats_publisher.py`
- **Extract subzone from room_id, returning 'unknown' if extraction fails.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build whisper subject; returns fallback 'chat.whisper' if no target_id.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build party subject; returns None if no party_id.** (1 connections) — `server/game/chat_nats_publisher.py`
- **System subject; personal system (quest lifecycle) routes like whisper when targe** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build NATS subject using standardized patterns via subject_manager.** (1 connections) — `server/game/chat_nats_publisher.py`
- *... and 11 more nodes in this community*

## Relationships

- [ChatMessage](ChatMessage.md) (14 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [test combat persistence handler events](test_combat_persistence_handler_events.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [PartyUpdated](PartyUpdated.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [get mythos time()](get_mythos_time%28%29.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/game/chat_validator.py`

## Audit Trail

- EXTRACTED: 134 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*