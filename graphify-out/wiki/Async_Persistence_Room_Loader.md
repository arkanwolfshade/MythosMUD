# Async Persistence Room Loader

> 66 nodes

## Key Concepts

- **RoomCacheLoader** (25 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_room_loader.py** (18 connections) — `server/async_persistence_room_loader.py`
- **AsyncPersistenceRoomFacade** (16 connections) — `server/async_persistence_room_facade.py`
- **ProcessedRoomData** (15 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_room_facade.py** (12 connections) — `server/async_persistence_room_facade.py`
- **ExitJsonEntry** (10 connections) — `server/async_persistence_room_loader.py`
- **RoomLoadResult** (10 connections) — `server/async_persistence_room_loader.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **test_async_persistence_room_rest_location.py** (9 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **._process_combined_rows()** (8 connections) — `server/async_persistence_room_loader.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence_room_facade.py`
- **._build_room_data_from_row()** (7 connections) — `server/async_persistence_room_loader.py`
- **_AsyncPersistenceRoomFacadeBase** (6 connections) — `server/async_persistence_room_facade.py`
- **RoomInitPayload** (6 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (6 connections) — `server/async_persistence_room_loader.py`
- **test_build_room_objects_defaults_rest_location_false()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_promotes_rest_location_from_attributes()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **._build_room_objects()** (5 connections) — `server/async_persistence_room_loader.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence_room_facade.py`
- **.__init__()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_exits_json()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_zone_parts()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence_room_loader.py`
- **_row_optional_str()** (4 connections) — `server/async_persistence_room_loader.py`
- *... and 41 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (8 shared connections)
- [Async Persistence](Async_Persistence.md) (5 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (2 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Player Effect Repository](Player_Effect_Repository.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)
- [Database](Database.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Audit Trail

- EXTRACTED: 143 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*