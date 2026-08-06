# event publisher realtime

> 79 nodes

## Key Concepts

- **EventPublisher** (29 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (25 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_helpers.py** (9 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **Any** (6 connections)
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_resolves_names_from_persistence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_resolves_names_from_persistence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_uses_legacy_subjects_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_uses_metadata_tick_number()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_returns_false_when_nats_publish_fails()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_async_persistence_handles_container_failure()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **mock_nats_service()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_subject_manager()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- *... and 54 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [spell models rationale](spell_models_rationale.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)
- [realtime player connection](realtime_player_connection.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 208 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*