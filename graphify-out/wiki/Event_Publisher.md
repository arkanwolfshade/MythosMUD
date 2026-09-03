# Event Publisher

> 11 nodes

## Key Concepts

- **_EventPersistence** (6 connections) — `server/realtime/event_publisher.py`
- **_NatsPublish** (5 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (5 connections) — `server/realtime/event_publisher.py`
- **_Named** (4 connections) — `server/realtime/event_publisher.py`
- **.get_player_by_id()** (3 connections) — `server/realtime/event_publisher.py`
- **Protocol** (3 connections)
- **.get_room_by_id()** (2 connections) — `server/realtime/event_publisher.py`
- **UUID** (2 connections)
- **.is_connected()** (1 connections) — `server/realtime/event_publisher.py`
- **.publish()** (1 connections) — `server/realtime/event_publisher.py`
- **Initialize EventPublisher service. Args: nats_service: NATS service instance…** (1 connections) — `server/realtime/event_publisher.py`

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Event Publisher](Event_Publisher.md) (2 shared connections)
- [Test Manager](Test_Manager.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*