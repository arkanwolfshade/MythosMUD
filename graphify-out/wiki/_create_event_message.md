# ._create_event_message

> 15 nodes

## Key Concepts

- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **Any** (6 connections)
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **Publish a player_left event to NATS. Args: player_id: ID of the player who left…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…** (1 connections) — `server/realtime/event_publisher.py`
- **Initialize EventPublisher service. Args: nats_service: NATS service instance…** (1 connections) — `server/realtime/event_publisher.py`
- **Create a standardized event message structure. Args: event_type: Type of event…** (1 connections) — `server/realtime/event_publisher.py`
- **Get the next sequence number for event ordering. Returns: Next sequence number** (1 connections) — `server/realtime/event_publisher.py`
- **Get async_persistence from ApplicationContainer (lazy-loaded).** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a player_entered event to NATS. Args: player_id: ID of the player who…** (1 connections) — `server/realtime/event_publisher.py`

## Relationships

- [EventPublisher](EventPublisher.md) (7 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*