# room persistence loader

> 26 nodes

## Key Concepts

- **RoomCacheLoader** (29 connections) — `server/async_persistence_room_loader.py`
- **Any** (12 connections)
- **.load()** (10 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **datetime** (6 connections)
- **._process_combined_rows()** (6 connections) — `server/async_persistence_room_loader.py`
- **._build_room_data_from_row()** (5 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (5 connections) — `server/async_persistence_room_loader.py`
- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **._parse_zone_parts()** (4 connections) — `server/async_persistence_room_loader.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence_room_loader.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence_room_loader.py`
- **._apply_rooms_to_cache()** (3 connections) — `server/async_persistence_room_loader.py`
- **._handle_room_load_error()** (3 connections) — `server/async_persistence_room_loader.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence_room_loader.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence_room_loader.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence_room_loader.py`
- **._extract_exit_fields()** (3 connections) — `server/async_persistence_room_loader.py`
- **._resolve_exit_room_ids()** (3 connections) — `server/async_persistence_room_loader.py`
- **._log_exit_debug()** (3 connections) — `server/async_persistence_room_loader.py`
- **.__init__()** (2 connections) — `server/async_persistence_room_loader.py`
- **._log_room_cache_after_load()** (2 connections) — `server/async_persistence_room_loader.py`
- **BaseException** (2 connections)
- **Get decayed containers.** (1 connections) — `server/async_persistence.py`
- **Loads room data from the database and populates a room cache dict.      Used by** (1 connections) — `server/async_persistence_room_loader.py`
- *... and 1 more nodes in this community*

## Relationships

- [npc populate databases](npc_populate_databases.md) (7 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 116 (90%)
- INFERRED: 13 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*