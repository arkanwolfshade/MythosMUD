# Any

> 32 nodes

## Key Concepts

- **EventPublisher** (23 connections) — `server/realtime/event_publisher.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **realtime.py** (12 connections) — `server/container/bundles/realtime.py`
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
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **Any** (1 connections)
- **Realtime bundle: NATS, connection manager, event handler, event publisher.  Depe** (1 connections) — `server/container/bundles/realtime.py`
- **Real-time communication: NATS, connection manager, event handler.** (1 connections) — `server/container/bundles/realtime.py`
- **Raise if any core dependency is missing.** (1 connections) — `server/container/bundles/realtime.py`
- **Connect to NATS if enabled and not unit_test. Returns NATSService or None.** (1 connections) — `server/container/bundles/realtime.py`
- **Attach event publisher and message handler when NATS is available.** (1 connections) — `server/container/bundles/realtime.py`
- **Initialize real-time services. Requires CoreBundle attributes on container.** (1 connections) — `server/container/bundles/realtime.py`
- **Service for publishing real-time game events to NATS subjects.      This service** (1 connections) — `server/realtime/event_publisher.py`
- **Initialize EventPublisher service.          Args:             nats_service: NATS** (1 connections) — `server/realtime/event_publisher.py`
- *... and 7 more nodes in this community*

## Relationships

- [test command parser](test_command_parser.md) (6 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (6 shared connections)
- [Player](Player.md) (5 shared connections)
- [world](world.md) (4 shared connections)
- [event publisher()](event_publisher%28%29.md) (4 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [circuit breaker](circuit_breaker.md) (3 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (3 shared connections)
- [handle explore command()](handle_explore_command%28%29.md) (2 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (1 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/event_publisher.py`

## Audit Trail

- EXTRACTED: 124 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*