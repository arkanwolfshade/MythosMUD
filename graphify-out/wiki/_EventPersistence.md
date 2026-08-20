# _EventPersistence

> 13 nodes

## Key Concepts

- **_EventPersistence** (5 connections) — `server/realtime/event_publisher.py`
- **_NatsPublish** (5 connections) — `server/realtime/event_publisher.py`
- **._get_async_persistence()** (5 connections) — `server/realtime/event_publisher.py`
- **_Named** (4 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_player_by_id()** (3 connections) — `server/realtime/event_publisher.py`
- **Protocol** (3 connections)
- **.get_room_by_id()** (2 connections) — `server/realtime/event_publisher.py`
- **UUID** (2 connections)
- **.is_connected()** (1 connections) — `server/realtime/event_publisher.py`
- **.publish()** (1 connections) — `server/realtime/event_publisher.py`
- **Get async_persistence from ApplicationContainer (lazy-loaded).** (1 connections) — `server/realtime/event_publisher.py`
- **Initialize EventPublisher service. Args: nats_service: NATS service instance…** (1 connections) — `server/realtime/event_publisher.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [EventPublisher](EventPublisher.md) (3 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*