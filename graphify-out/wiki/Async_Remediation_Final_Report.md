# Async Remediation Final Report

> 27 nodes · cohesion 0.14

## Key Concepts

- **RoomCacheLoader** (26 connections) — `server/async_persistence_room_loader.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (9 connections) — `server/async_persistence_room_loader.py`
- **._build_room_data_from_row()** (8 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **.__init__()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_zone_parts()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence_room_loader.py`
- **_row_optional_float()** (4 connections) — `server/async_persistence_room_loader.py`
- **_row_optional_str()** (4 connections) — `server/async_persistence_room_loader.py`
- **_attributes_from_row()** (3 connections) — `server/async_persistence_room_loader.py`
- **Room** (3 connections)
- **._apply_rooms_to_cache()** (3 connections) — `server/async_persistence_room_loader.py`
- **._extract_exit_fields()** (3 connections) — `server/async_persistence_room_loader.py`
- **._handle_room_load_error()** (3 connections) — `server/async_persistence_room_loader.py`
- **._log_exit_debug()** (3 connections) — `server/async_persistence_room_loader.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_loader.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_loader.py`
- **._resolve_exit_room_ids()** (3 connections) — `server/async_persistence_room_loader.py`
- **._log_room_cache_after_load()** (2 connections) — `server/async_persistence_room_loader.py`
- **AsyncSession** (1 connections)
- **BaseException** (1 connections)
- **BoundLogger** (1 connections)
- **Loads room data from the database and populates a room cache dict. Used by…** (1 connections) — `server/async_persistence_room_loader.py`
- *... and 2 more nodes in this community*

## Relationships

- [FastAPI Code Review - Anti-Patterns and Best Practices](FastAPI_Code_Review_-_Anti-Patterns_and_Best_Practices.md) (14 shared connections)
- [test_inventory_item_matching.py](test_inventory_item_matching.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)
- [Real-World Impact for MythosMUD](Real-World_Impact_for_MythosMUD.md) (1 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)
- [compilerOptions](compilerOptions.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 67 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*