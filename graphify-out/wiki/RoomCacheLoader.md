# RoomCacheLoader

> 23 nodes

## Key Concepts

- **RoomCacheLoader** (24 connections) — `server/async_persistence_room_loader.py`
- **Any** (11 connections)
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (6 connections) — `server/async_persistence_room_loader.py`
- **._build_room_data_from_row()** (5 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (5 connections) — `server/async_persistence_room_loader.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_zone_parts()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence_room_loader.py`
- **._apply_rooms_to_cache()** (3 connections) — `server/async_persistence_room_loader.py`
- **._extract_exit_fields()** (3 connections) — `server/async_persistence_room_loader.py`
- **._handle_room_load_error()** (3 connections) — `server/async_persistence_room_loader.py`
- **._log_exit_debug()** (3 connections) — `server/async_persistence_room_loader.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence_room_loader.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_loader.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_loader.py`
- **._resolve_exit_room_ids()** (3 connections) — `server/async_persistence_room_loader.py`
- **.__init__()** (2 connections) — `server/async_persistence_room_loader.py`
- **._log_room_cache_after_load()** (2 connections) — `server/async_persistence_room_loader.py`
- **BaseException** (1 connections)
- **Loads room data from the database and populates a room cache dict. Used by…** (1 connections) — `server/async_persistence_room_loader.py`
- **Load rooms from PostgreSQL and update the room cache.** (1 connections) — `server/async_persistence_room_loader.py`

## Relationships

- [pytest.md](pytest.md.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 57 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*