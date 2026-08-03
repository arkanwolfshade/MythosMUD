# room rationale subzone

> 80 nodes

## Key Concepts

- **chat_nats_publisher.py** (29 connections) — `server/game/chat_nats_publisher.py`
- **test_room_utils.py** (22 connections) — `server/tests/unit/utils/test_room_utils.py`
- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **_build_standardized_subject()** (9 connections) — `server/game/chat_nats_publisher.py`
- **chat_validator.py** (9 connections) — `server/game/chat_validator.py`
- **room_utils.py** (9 connections) — `server/utils/room_utils.py`
- **Any** (8 connections)
- **build_nats_subject()** (6 connections) — `server/game/chat_nats_publisher.py`
- **get_zone_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **get_plane_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **get_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **get_subzone_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **_extract_subzone_from_room()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_whisper_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_subject_system_standardized()** (5 connections) — `server/game/chat_nats_publisher.py`
- **_chat_passes_nats_validation()** (5 connections) — `server/game/chat_nats_publisher.py`
- **validate_chat_message()** (5 connections) — `server/game/chat_validator.py`
- **is_valid_room_id_format()** (5 connections) — `server/utils/room_utils.py`
- **_subject_party_standardized()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_legacy_subject()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_nats_service_ready()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_build_nats_message_data()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_publish_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **_log_nats_unexpected_error()** (4 connections) — `server/game/chat_nats_publisher.py`
- **validate_room_access()** (4 connections) — `server/game/chat_validator.py`
- *... and 55 more nodes in this community*

## Relationships

- [chat game message](chat_game_message.md) (16 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (3 shared connections)
- [subject validation services](subject_validation_services.md) (2 shared connections)
- [item models rationale](item_models_rationale.md) (2 shared connections)
- [quest chat game](quest_chat_game.md) (1 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (1 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (1 shared connections)
- [chat services logger](chat_services_logger.md) (1 shared connections)

## Source Files

- `server/game/chat_nats_publisher.py`
- `server/game/chat_validator.py`
- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 273 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*