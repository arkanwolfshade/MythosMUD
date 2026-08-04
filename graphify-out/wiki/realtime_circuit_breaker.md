# realtime circuit breaker

> 15 nodes

## Key Concepts

- **RoomRepositoryProtocol** (13 connections) — `server/persistence/protocols.py`
- **protocols.py** (12 connections) — `server/persistence/protocols.py`
- **test_protocols.py** (10 connections) — `server/tests/unit/persistence/test_protocols.py`
- **_StubRoomRepo** (6 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_room_repository_protocol_stub()** (5 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_room_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.list_rooms()** (4 connections) — `server/persistence/protocols.py`
- **Room** (2 connections)
- **.get_room_by_id()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.list_rooms()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **Repository protocols for MythosMUD persistence layer.  Explicit typing.Protocol** (1 connections) — `server/persistence/protocols.py`
- **Protocol for room persistence operations.      Defines the contract used by Asyn** (1 connections) — `server/persistence/protocols.py`
- **Get a room by ID from cache.** (1 connections) — `server/persistence/protocols.py`
- **List all cached rooms.** (1 connections) — `server/persistence/protocols.py`
- **Runtime checks for persistence repository protocols.** (1 connections) — `server/tests/unit/persistence/test_protocols.py`

## Relationships

- [persistence protocols rationale](persistence_protocols_rationale.md) (9 shared connections)
- [config models game](config_models_game.md) (4 shared connections)
- [combat models rationale](combat_models_rationale.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [persistence container item](persistence_container_item.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 57 (88%)
- INFERRED: 8 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*