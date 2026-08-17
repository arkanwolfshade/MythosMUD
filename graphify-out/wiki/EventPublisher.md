# EventPublisher

> 20 nodes

## Key Concepts

- **EventPublisher** (32 connections) — `server/realtime/event_publisher.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (7 connections) — `server/realtime/event_publisher.py`
- **._get_async_persistence()** (5 connections) — `server/realtime/event_publisher.py`
- **._publish_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (5 connections) — `server/realtime/event_publisher.py`
- **JsonMap** (5 connections)
- **._resolve_player_and_room_names()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **._player_event_subject()** (3 connections) — `server/realtime/event_publisher.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **Publish a player_entered event to NATS. Args: player_id: ID of the player who…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a player_left event to NATS. Args: player_id: ID of the player who left…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…** (1 connections) — `server/realtime/event_publisher.py`
- **Create a standardized event message structure. Args: event_type: Type of event…** (1 connections) — `server/realtime/event_publisher.py`
- **Get the next sequence number for event ordering. Returns: Next sequence number** (1 connections) — `server/realtime/event_publisher.py`
- **Reset the sequence number to 0.** (1 connections) — `server/realtime/event_publisher.py`
- **Get async_persistence from ApplicationContainer (lazy-loaded).** (1 connections) — `server/realtime/event_publisher.py`
- **Service for publishing real-time game events to NATS subjects. This service…** (1 connections) — `server/realtime/event_publisher.py`

## Relationships

- [test_event_publisher.py](test_event_publisher.py.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_event_publisher_helpers.py](test_event_publisher_helpers.py.md) (2 shared connections)
- [_EventPersistence](_EventPersistence.md) (2 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [event_publisher](event_publisher.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`

## Audit Trail

- EXTRACTED: 46 (79%)
- INFERRED: 12 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*