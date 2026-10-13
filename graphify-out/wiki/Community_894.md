# Community 894

> 17 nodes

## Key Concepts

- **RoomLoadResult** (13 connections) — `server/async_persistence_room_loader.py`
- **test_async_persistence_room_rest_location.py** (12 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **RoomInitPayload** (9 connections) — `server/async_persistence_room_loader.py`
- **test_build_room_objects_carries_display_names()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_carries_map_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_defaults_rest_location_false()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_promotes_rest_location_from_attributes()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_tolerates_missing_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **TypedDict** (4 connections)
- **Mutable container passed through room object construction.** (1 connections) — `server/async_persistence_room_loader.py`
- **Payload passed to Room.__init__ during cache load.** (1 connections) — `server/async_persistence_room_loader.py`
- **Unit tests for _build_room_objects' rest_location promotion (#297). Split out…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **A room with no coordinates must still load - the keys are present and null, not…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **#910: zone/sub-zone display names must survive ProcessedRoomData ->…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **#297: rest_location lives in the JSONB attributes column (DML), not a top-level…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **A room with no rest_location attribute must not silently become a rest location.** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **#829: map_x/map_y must survive the ProcessedRoomData -> RoomInitPayload hop.…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Relationships

- [Community 814](Community_814.md) (10 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (4 shared connections)
- [Community 587](Community_587.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_loader.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Audit Trail

- EXTRACTED: 28 (57%)
- INFERRED: 21 (43%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*