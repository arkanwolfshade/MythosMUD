# event publisher realtime

> 83 nodes

## Key Concepts

- **EventPublisher** (29 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (25 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_helpers.py** (9 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **._setup_nats_dependent_services()** (6 connections) — `server/container/bundles/realtime.py`
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
- *... and 58 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (1 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 223 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*