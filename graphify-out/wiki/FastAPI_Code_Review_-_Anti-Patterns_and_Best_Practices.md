# FastAPI Code Review - Anti-Patterns and Best Practices

> 40 nodes · cohesion 0.11

## Key Concepts

- **async_persistence_room_loader.py** (23 connections) — `server/async_persistence_room_loader.py`
- **ProcessedRoomData** (21 connections) — `server/async_persistence_room_loader.py`
- **AsyncPersistenceRoomFacade** (16 connections) — `server/async_persistence_room_facade.py`
- **async_persistence_room_facade.py** (13 connections) — `server/async_persistence_room_facade.py`
- **RoomLoadResult** (13 connections) — `server/async_persistence_room_loader.py`
- **test_async_persistence_room_rest_location.py** (12 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **ExitJsonEntry** (10 connections) — `server/async_persistence_room_loader.py`
- **RoomInitPayload** (9 connections) — `server/async_persistence_room_loader.py`
- **test_build_room_objects_carries_display_names()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_carries_map_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_defaults_rest_location_false()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_promotes_rest_location_from_attributes()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **test_build_room_objects_tolerates_missing_coordinates()** (6 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`
- **._build_room_objects()** (5 connections) — `server/async_persistence_room_loader.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence_room_facade.py`
- **TypedDict** (4 connections)
- **._parse_exits_json()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_combined_rows()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_exits_for_room()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_facade.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_facade.py`
- **_coerce_exit_entries()** (3 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (2 connections) — `server/async_persistence_room_facade.py`
- **._process_exit_rows()** (2 connections) — `server/async_persistence_room_facade.py`
- *... and 15 more nodes in this community*

## Relationships

- [Async Remediation Final Report](Async_Remediation_Final_Report.md) (14 shared connections)
- [test_party_service.py](test_party_service.py.md) (7 shared connections)
- [Room](Room.md) (4 shared connections)
- [asyncio](asyncio.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (2 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [Real-World Impact for MythosMUD](Real-World_Impact_for_MythosMUD.md) (2 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [compilerOptions](compilerOptions.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_rest_location.py`

## Audit Trail

- EXTRACTED: 101 (80%)
- INFERRED: 25 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*