# Community 587

> 29 nodes

## Key Concepts

- **RoomCacheLoader** (26 connections) — `server/async_persistence_room_loader.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (9 connections) — `server/async_persistence_room_loader.py`
- **._build_room_data_from_row()** (8 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **._build_room_objects()** (5 connections) — `server/async_persistence_room_loader.py`
- **.__init__()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_zone_parts()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence_room_loader.py`
- **_row_optional_float()** (4 connections) — `server/async_persistence_room_loader.py`
- **_row_optional_str()** (4 connections) — `server/async_persistence_room_loader.py`
- **_attributes_from_row()** (3 connections) — `server/async_persistence_room_loader.py`
- **._apply_rooms_to_cache()** (3 connections) — `server/async_persistence_room_loader.py`
- **._extract_exit_fields()** (3 connections) — `server/async_persistence_room_loader.py`
- **._handle_room_load_error()** (3 connections) — `server/async_persistence_room_loader.py`
- **._log_exit_debug()** (3 connections) — `server/async_persistence_room_loader.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_loader.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_loader.py`
- **._resolve_exit_room_ids()** (3 connections) — `server/async_persistence_room_loader.py`
- **Room** (3 connections)
- **._log_room_cache_after_load()** (2 connections) — `server/async_persistence_room_loader.py`
- **AsyncSession** (1 connections)
- **BaseException** (1 connections)
- **BoundLogger** (1 connections)
- *... and 4 more nodes in this community*

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (7 shared connections)
- [Community 814](Community_814.md) (7 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 894](Community_894.md) (1 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (1 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (1 shared connections)

## Source Files

- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 69 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*