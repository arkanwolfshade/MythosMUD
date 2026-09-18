# Community 759

> 22 nodes

## Key Concepts

- **EventPublisher** (29 connections) — `server/realtime/event_publisher.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (7 connections) — `server/realtime/event_publisher.py`
- **._publish_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (5 connections) — `server/realtime/event_publisher.py`
- **JsonMap** (5 connections)
- **._get_async_persistence()** (4 connections) — `server/realtime/event_publisher.py`
- **._resolve_player_and_room_names()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **._player_event_subject()** (3 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **Publish a player_entered event to NATS. Args: player_id: ID of the player who…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a player_left event to NATS. Args: player_id: ID of the player who left…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…** (1 connections) — `server/realtime/event_publisher.py`
- **Create a standardized event message structure. Args: event_type: Type of event…** (1 connections) — `server/realtime/event_publisher.py`
- **Get the next sequence number for event ordering. Returns: Next sequence number** (1 connections) — `server/realtime/event_publisher.py`
- **Reset the sequence number to 0.** (1 connections) — `server/realtime/event_publisher.py`
- **Get async_persistence (#679: injected at construction by RealtimeBundle).** (1 connections) — `server/realtime/event_publisher.py`
- **Service for publishing real-time game events to NATS subjects. This service…** (1 connections) — `server/realtime/event_publisher.py`
- **Test EventPublisher initialization without subject manager.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`

## Relationships

- [Community 522](Community_522.md) (7 shared connections)
- [Community 87](Community_87.md) (3 shared connections)
- [Community 1425](Community_1425.md) (2 shared connections)
- [Community 972](Community_972.md) (2 shared connections)
- [Community 1137](Community_1137.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)
- [Community 28](Community_28.md) (1 shared connections)
- [Community 1363](Community_1363.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 48 (86%)
- INFERRED: 8 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*