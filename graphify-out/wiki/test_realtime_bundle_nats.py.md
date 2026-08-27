# test_realtime_bundle_nats.py

> 16 nodes

## Key Concepts

- **test_protocols.py** (11 connections) — `server/tests/unit/persistence/test_protocols.py`
- **RoomRepositoryProtocol** (10 connections) — `server/persistence/protocols.py`
- **test_player_repository_protocol_stub()** (5 connections) — `server/tests/unit/persistence/test_protocols.py`
- **_StubRoomRepo** (4 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_room_by_id()** (4 connections) — `server/persistence/protocols.py`
- **.list_rooms()** (4 connections) — `server/persistence/protocols.py`
- **test_room_repository_protocol_stub()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **Protocol** (2 connections)
- **Room** (2 connections)
- **asyncio** (2 connections)
- **.get_room_by_id()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.list_rooms()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **List all cached rooms.** (1 connections) — `server/persistence/protocols.py`
- **Protocol for room persistence operations. Defines the contract used by…** (1 connections) — `server/persistence/protocols.py`
- **Get a room by ID from cache.** (1 connections) — `server/persistence/protocols.py`
- **Runtime checks for persistence repository protocols.** (1 connections) — `server/tests/unit/persistence/test_protocols.py`

## Relationships

- [test_quality_fragmentation_guard.py](test_quality_fragmentation_guard.py.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [properties](properties.md) (3 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (1 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (1 shared connections)

## Source Files

- `server/persistence/protocols.py`
- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 30 (86%)
- INFERRED: 5 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*