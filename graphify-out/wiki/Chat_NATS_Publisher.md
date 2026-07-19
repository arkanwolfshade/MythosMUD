# Chat NATS Publisher

> 37 nodes · cohesion 0.08

## Key Concepts

- **chat_nats_publisher.py** (21 connections) — `server/game/chat_nats_publisher.py`
- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **chat_pose_helpers.py** (14 connections) — `server/game/chat_pose_helpers.py`
- **set_player_pose()** (8 connections) — `server/game/chat_pose_helpers.py`
- **_build_standardized_subject()** (7 connections) — `server/game/chat_nats_publisher.py`
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **Any** (6 connections) — `server/game/chat_nats_publisher.py`
- **Any** (6 connections) — `server/game/chat_pose_helpers.py`
- **_extract_subzone_from_room()** (5 connections) — `server/game/chat_nats_publisher.py`
- **clear_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **get_player_pose()** (5 connections) — `server/game/chat_pose_helpers.py`
- **validate_chat_message()** (5 connections) — `server/game/chat_validator.py`
- **UUID** (5 connections) — `server/game/chat_pose_helpers.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **get_room_poses()** (4 connections) — `server/game/chat_pose_helpers.py`
- **normalize_player_id()** (4 connections) — `server/game/chat_pose_helpers.py`
- **validate_room_access()** (4 connections) — `server/game/chat_validator.py`
- **contains_malicious_content()** (3 connections) — `server/game/chat_validator.py`
- **Chat NATS publishing utilities.  This module provides NATS subject building and** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build NATS subject using standardized patterns or fallback to legacy constructio** (1 connections) — `server/game/chat_nats_publisher.py`
- **Extract subzone from room_id, returning 'unknown' if extraction fails.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build whisper subject; returns fallback 'chat.whisper' if no target_id.** (1 connections) — `server/game/chat_nats_publisher.py`
- **Build party subject; returns None if no party_id.** (1 connections) — `server/game/chat_nats_publisher.py`
- *... and 12 more nodes in this community*

## Relationships

- [[Chat Message Helpers]] (20 shared connections)
- [[NPC Admin API]] (11 shared connections)
- [[Room Get Zone Id]] (4 shared connections)
- [[Combat Domain Events]] (2 shared connections)
- [[NATS Subject Exceptions]] (1 shared connections)
- [[Distributed Event Bus]] (1 shared connections)
- [[NPC Movement Integration]] (1 shared connections)
- [[NATS Chat Broadcasting]] (1 shared connections)
- [[Chat Channel Logger]] (1 shared connections)
- [[Room Services Validator]] (1 shared connections)
- [[Room Get Subzone Local]] (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_validator.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 149 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
