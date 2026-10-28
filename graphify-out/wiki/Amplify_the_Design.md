# Amplify the Design

> 11 nodes · cohesion 0.24

## Key Concepts

- **_EventPersistence** (6 connections) — `server/realtime/event_publisher.py`
- **.__init__()** (5 connections) — `server/realtime/event_publisher.py`
- **_NatsPublish** (5 connections) — `server/realtime/event_publisher.py`
- **_Named** (4 connections) — `server/realtime/event_publisher.py`
- **.get_player_by_id()** (3 connections) — `server/realtime/event_publisher.py`
- **Protocol** (3 connections)
- **.get_room_by_id()** (2 connections) — `server/realtime/event_publisher.py`
- **UUID** (2 connections)
- **.is_connected()** (1 connections) — `server/realtime/event_publisher.py`
- **.publish()** (1 connections) — `server/realtime/event_publisher.py`
- **Initialize EventPublisher service. Args: nats_service: NATS service instance…** (1 connections) — `server/realtime/event_publisher.py`

## Relationships

- [Room](Room.md) (4 shared connections)
- [MythosMUD Code Quality Targets for AI](MythosMUD_Code_Quality_Targets_for_AI.md) (2 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*