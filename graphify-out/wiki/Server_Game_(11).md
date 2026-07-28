# Server Game (11)

> 72 nodes

## Key Concepts

- **ChatMessage** (31 connections) — `server/game/chat_message.py`
- **chat_nats_publisher.py** (20 connections) — `server/game/chat_nats_publisher.py`
- **chat_service.py** (14 connections) — `server/game/chat_service.py`
- **chat_pose_helpers.py** (13 connections) — `server/game/chat_pose_helpers.py`
- **chat_message.py** (12 connections) — `server/game/chat_message.py`
- **Any** (8 connections)
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **set_player_pose()** (7 connections) — `server/game/chat_pose_helpers.py`
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **Any** (5 connections)
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **normalize_player_id()** (4 connections) — `server/game/chat_pose_helpers.py`
- **UUID** (4 connections)
- **get_player_pose()** (4 connections) — `server/game/chat_pose_helpers.py`
- **clear_player_pose()** (4 connections) — `server/game/chat_pose_helpers.py`
- **_extract_subzone_from_room()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_nats_service_ready()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_unexpected_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **get_room_poses()** (3 connections) — `server/game/chat_pose_helpers.py`
- **test_chat_message_to_dict_includes_speaker_kind()** (3 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- *... and 47 more nodes in this community*

## Relationships

- [Server Game (22)](Server_Game_%2822%29.md) (21 shared connections)
- [Server Game (12)](Server_Game_%2812%29.md) (12 shared connections)
- [Server Game (16)](Server_Game_%2816%29.md) (9 shared connections)
- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server App](Server_App.md) (1 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)
- [Server Game (13)](Server_Game_%2813%29.md) (1 shared connections)
- [Server Events](Server_Events.md) (1 shared connections)

## Source Files

- `server/game/chat_message.py`
- `server/game/chat_nats_publisher.py`
- `server/game/chat_pose_helpers.py`
- `server/game/chat_service.py`
- `server/tests/unit/game/test_chat_npc_system.py`
- `server/tests/unit/game/test_chat_service.py`
- `vulture_allowlist.py`

## Audit Trail

- EXTRACTED: 249 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*