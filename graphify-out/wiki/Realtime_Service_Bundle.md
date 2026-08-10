# Realtime Service Bundle

> 15 nodes

## Key Concepts

- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **Any** (6 connections)
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **Initialize EventPublisher service.          Args:             nats_service: NATS** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a player_entered event to NATS.          Args:             player_id: ID** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a player_left event to NATS.          Args:             player_id: ID of** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a game_tick event to NATS.          Args:             timestamp: Optiona** (1 connections) — `server/realtime/event_publisher.py`
- **Create a standardized event message structure.          Args:             event_** (1 connections) — `server/realtime/event_publisher.py`
- **Get the next sequence number for event ordering.          Returns:             N** (1 connections) — `server/realtime/event_publisher.py`
- **Get async_persistence from ApplicationContainer (lazy-loaded).** (1 connections) — `server/realtime/event_publisher.py`

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (7 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*