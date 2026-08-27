# .load_container_from_room_json

> 28 nodes

## Key Concepts

- **EventPublisher** (32 connections) — `server/realtime/event_publisher.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (7 connections) — `server/realtime/event_publisher.py`
- **._publish_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (5 connections) — `server/realtime/event_publisher.py`
- **JsonMap** (5 connections)
- **._get_async_persistence()** (4 connections) — `server/realtime/event_publisher.py`
- **._resolve_player_and_room_names()** (4 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **._player_event_subject()** (3 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_async_persistence_returns_none_when_unset()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **Initialize the connection manager with modular components.** (1 connections) — `server/realtime/connection_manager.py`
- **Publish a player_entered event to NATS. Args: player_id: ID of the player who…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a player_left event to NATS. Args: player_id: ID of the player who left…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…** (1 connections) — `server/realtime/event_publisher.py`
- **Create a standardized event message structure. Args: event_type: Type of event…** (1 connections) — `server/realtime/event_publisher.py`
- **Get the next sequence number for event ordering. Returns: Next sequence number** (1 connections) — `server/realtime/event_publisher.py`
- **Reset the sequence number to 0.** (1 connections) — `server/realtime/event_publisher.py`
- **Get async_persistence (#679: injected at construction by RealtimeBundle).** (1 connections) — `server/realtime/event_publisher.py`
- **Service for publishing real-time game events to NATS subjects. This service…** (1 connections) — `server/realtime/event_publisher.py`
- *... and 3 more nodes in this community*

## Relationships

- [Uplift Strategy](Uplift_Strategy.md) (10 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [Asynchronous Code Audit - December 3, 2025](Asynchronous_Code_Audit_-_December_3,_2025.md) (2 shared connections)
- [PopulationStats](PopulationStats.md) (2 shared connections)
- [✅ Phase 2 Async Persistence Migration - COMPLETE](✅_Phase_2_Async_Persistence_Migration_-_COMPLETE.md) (1 shared connections)
- [Shared JSON schemas](Shared_JSON_schemas.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 56 (86%)
- INFERRED: 9 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*