# Server Realtime (16)

> 81 nodes

## Key Concepts

- **EventPublisher** (20 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (19 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **realtime.py** (12 connections) — `server/container/bundles/realtime.py`
- **test_event_publisher_helpers.py** (9 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **._setup_nats_dependent_services()** (6 connections) — `server/container/bundles/realtime.py`
- **Any** (6 connections)
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **._connect_nats()** (5 connections) — `server/container/bundles/realtime.py`
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/realtime.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **.shutdown()** (3 connections) — `server/container/bundles/realtime.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **mock_nats_service()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_subject_manager()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- *... and 56 more nodes in this community*

## Relationships

- [Server App (2)](Server_App_%282%29.md) (6 shared connections)
- [Server App](Server_App.md) (6 shared connections)
- [Server Commands](Server_Commands.md) (6 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (3 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (3 shared connections)
- [Server Realtime](Server_Realtime.md) (3 shared connections)
- [Server Services (2)](Server_Services_%282%29.md) (3 shared connections)
- [Server Services (3)](Server_Services_%283%29.md) (2 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 226 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*