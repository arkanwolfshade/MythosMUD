# Async Persistence Types

> 35 nodes · cohesion 0.11

## Key Concepts

- **RoomCacheLoader** (33 connections) — `server/async_persistence_room_loader.py`
- **CreateItemInstanceInput** (14 connections) — `server/async_persistence_constants.py`
- **Any** (12 connections) — `server/async_persistence_room_loader.py`
- **.load()** (9 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **._process_combined_rows()** (6 connections) — `server/async_persistence_room_loader.py`
- **Profession** (5 connections) — `server/async_persistence.py`
- **._build_room_data_from_row()** (5 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (5 connections) — `server/async_persistence_room_loader.py`
- **CreateItemInstanceInput** (4 connections) — `server/async_persistence.py`
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.get_user_by_username_case_insensitive()** (4 connections) — `server/async_persistence.py`
- **ContainerCreateParams** (4 connections) — `server/async_persistence.py`
- **User** (4 connections) — `server/async_persistence.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence_room_loader.py`
- **._parse_zone_parts()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence_room_loader.py`
- **async_persistence_constants.py** (3 connections) — `server/async_persistence_constants.py`
- **._apply_rooms_to_cache()** (3 connections) — `server/async_persistence_room_loader.py`
- **._extract_exit_fields()** (3 connections) — `server/async_persistence_room_loader.py`
- **._handle_room_load_error()** (3 connections) — `server/async_persistence_room_loader.py`
- **._log_exit_debug()** (3 connections) — `server/async_persistence_room_loader.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence_room_loader.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_loader.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_loader.py`
- *... and 10 more nodes in this community*

## Relationships

- [[NPC Admin API]] (19 shared connections)
- [[Async Persistence Layer]] (13 shared connections)
- [[Dependency Risk Analyzer]] (1 shared connections)
- [[Room Occupancy Class]] (1 shared connections)
- [[Emote Schema Validator]] (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 132 (79%)
- INFERRED: 35 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
