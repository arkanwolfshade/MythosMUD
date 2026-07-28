# Server Persistence (18)

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

- [Server Services](Server_Services.md) (2 shared connections)
- [Server Persistence (10)](Server_Persistence_%2810%29.md) (1 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)
- [Server Models (23)](Server_Models_%2823%29.md) (1 shared connections)
- [Server Persistence (16)](Server_Persistence_%2816%29.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`

## Audit Trail

- EXTRACTED: 20 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*