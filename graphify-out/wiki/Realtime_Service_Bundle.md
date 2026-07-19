# Realtime Service Bundle

> 81 nodes · cohesion 0.03

## Key Concepts

- **EventPublisher** (22 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (18 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **realtime.py** (10 connections) — `server/container/bundles/realtime.py`
- **ApplicationContainer** (9 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **test_event_publisher_helpers.py** (8 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **Any** (7 connections) — `server/container/bundles/realtime.py`
- **Any** (6 connections) — `server/realtime/event_publisher.py`
- **._connect_nats()** (5 connections) — `server/container/bundles/realtime.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/realtime.py`
- **._setup_nats_dependent_services()** (5 connections) — `server/container/bundles/realtime.py`
- **._get_async_persistence()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **.shutdown()** (3 connections) — `server/container/bundles/realtime.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- *... and 56 more nodes in this community*

## Relationships

- [[Application DI Bundles]] (8 shared connections)
- [[Room Occupant Events]] (6 shared connections)
- [[Realtime Event Delegation]] (5 shared connections)
- [[NATS Chat Broadcasting]] (5 shared connections)
- [[Combat Domain Events]] (5 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Game Service Bundle]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 226 (91%)
- INFERRED: 22 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
