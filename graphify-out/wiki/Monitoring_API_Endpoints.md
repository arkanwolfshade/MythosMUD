# Monitoring API Endpoints

> 59 nodes

## Key Concepts

- **test_room_utils.py** (22 connections) — `server/tests/unit/utils/test_room_utils.py`
- **chat_nats_publisher.py** (21 connections) — `server/game/chat_nats_publisher.py`
- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **room_utils.py** (9 connections) — `server/utils/room_utils.py`
- **_build_standardized_subject()** (8 connections) — `server/game/chat_nats_publisher.py`
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **get_zone_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **get_plane_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **get_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **get_subzone_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **_extract_subzone_from_room()** (5 connections) — `server/game/chat_nats_publisher.py`
- **Any** (5 connections)
- **is_valid_room_id_format()** (5 connections) — `server/utils/room_utils.py`
- **_subject_whisper_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **test_extract_subzone_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_extract_subzone_from_room_id_downtown()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_extract_subzone_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id_innsmouth()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_plane_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_plane_from_room_id_dream()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_plane_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- *... and 34 more nodes in this community*

## Relationships

- [Chat Message Helpers](Chat_Message_Helpers.md) (7 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (3 shared connections)
- [E 2 E Timeout Analysis](E_2_E_Timeout_Analysis.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [Cursor Rules Docker](Cursor_Rules_Docker.md) (2 shared connections)
- [Player Effects API](Player_Effects_API.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 202 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*