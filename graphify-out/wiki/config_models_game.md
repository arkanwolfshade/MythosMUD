# config models game

> 8 nodes

## Key Concepts

- **RoomRepositoryProtocol** (9 connections) — `server/persistence/protocols.py`
- **.get_room_by_id()** (3 connections) — `server/persistence/protocols.py`
- **.list_rooms()** (3 connections) — `server/persistence/protocols.py`
- **Protocol** (2 connections)
- **Room** (2 connections)
- **Protocol for room persistence operations.      Defines the contract used by Asyn** (1 connections) — `server/persistence/protocols.py`
- **Get a room by ID from cache.** (1 connections) — `server/persistence/protocols.py`
- **List all cached rooms.** (1 connections) — `server/persistence/protocols.py`

## Relationships

- [persistence protocols rationale](persistence_protocols_rationale.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`

## Audit Trail

- EXTRACTED: 20 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*