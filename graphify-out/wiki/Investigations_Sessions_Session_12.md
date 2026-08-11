# Investigations Sessions Session

> 13 nodes

## Key Concepts

- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **_extract_subzone_from_room()** (5 connections) — `server/game/chat_nats_publisher.py`
- **Any** (5 connections)
- **_subject_whisper_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **Extract subzone from room_id, returning 'unknown' if extraction fails.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build whisper subject; returns fallback 'chat.whisper' if no target_id.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build party subject; returns None if no party_id.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build NATS subject using standardized patterns via subject_manager.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build NATS subject using legacy construction (backward compatibility).** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build NATS subject using standardized patterns or fallback to legacy constructio** (1 connections) — `server/game/chat_nats_publisher.py`

## Relationships

- [Who Command Tests](Who_Command_Tests.md) (8 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (1 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*