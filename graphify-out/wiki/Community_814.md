# Community 814

> 20 nodes

## Key Concepts

- **ProcessedRoomData** (21 connections) — `server/async_persistence_room_loader.py`
- **AsyncPersistenceRoomFacade** (14 connections) — `server/async_persistence_room_facade.py`
- **ExitJsonEntry** (10 connections) — `server/async_persistence_room_loader.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence_room_facade.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence_room_facade.py`
- **._parse_exits_json()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_combined_rows()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_exits_for_room()** (3 connections) — `server/async_persistence_room_facade.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_facade.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_facade.py`
- **_coerce_exit_entries()** (3 connections) — `server/async_persistence_room_loader.py`
- **test_build_room_objects_without_environment_in_attributes()** (3 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`
- **._generate_room_id_from_zone_data()** (2 connections) — `server/async_persistence_room_facade.py`
- **._process_exit_rows()** (2 connections) — `server/async_persistence_room_facade.py`
- **AsyncSession** (1 connections)
- **Mixin: lazy room-cache load and loader delegation for unit tests.** (1 connections) — `server/async_persistence_room_facade.py`
- **One exit entry from get_rooms_with_exits exits JSON.** (1 connections) — `server/async_persistence_room_loader.py`
- **Intermediate room row after zone/id normalization.** (1 connections) — `server/async_persistence_room_loader.py`
- **Test _build_room_objects passes through a NULL room_environment (inherited)…** (1 connections) — `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Relationships

- [Community 894](Community_894.md) (10 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (7 shared connections)
- [Community 587](Community_587.md) (7 shared connections)
- [Community 349](Community_349.md) (2 shared connections)
- [Community 1845](Community_1845.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/tests/unit/infrastructure/test_async_persistence_room_loading.py`

## Audit Trail

- EXTRACTED: 49 (83%)
- INFERRED: 10 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*