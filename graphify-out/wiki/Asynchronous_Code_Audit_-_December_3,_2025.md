# Asynchronous Code Audit - December 3, 2025

> 12 nodes

## Key Concepts

- **_EventPersistence** (6 connections) — `server/realtime/event_publisher.py`
- **_NatsPublish** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (5 connections) — `server/realtime/event_publisher.py`
- **_Named** (4 connections) — `server/realtime/event_publisher.py`
- **.get_player_by_id()** (3 connections) — `server/realtime/event_publisher.py`
- **Protocol** (3 connections)
- **.get_room_by_id()** (2 connections) — `server/realtime/event_publisher.py`
- **.is_connected()** (2 connections) — `server/realtime/event_publisher.py`
- **UUID** (2 connections)
- **.publish()** (1 connections) — `server/realtime/event_publisher.py`
- **NATSSubjectManager** (1 connections)
- **Initialize EventPublisher service. Args: nats_service: NATS service instance…** (1 connections) — `server/realtime/event_publisher.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [.load_container_from_room_json](load_container_from_room_json.md) (2 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*