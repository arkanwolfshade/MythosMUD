# Client Security Utilities

> 146 nodes

## Key Concepts

- **AsyncPersistenceLayer** (185 connections) — `server/async_persistence.py`
- **RoomCacheLoader** (29 connections) — `server/async_persistence_room_loader.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **Any** (20 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **Any** (12 connections)
- **.load()** (10 connections) — `server/async_persistence_room_loader.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **.get_player_by_id()** (6 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (6 connections) — `server/async_persistence_room_loader.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **._build_room_data_from_row()** (5 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (5 connections) — `server/async_persistence_room_loader.py`
- **conftest.py** (5 connections) — `server/tests/unit/infrastructure/conftest.py`
- **._process_exit_rows()** (4 connections) — `server/async_persistence.py`
- **._build_room_objects()** (4 connections) — `server/async_persistence.py`
- **._query_rooms_with_exits_async()** (4 connections) — `server/async_persistence.py`
- **._parse_exits_json()** (4 connections) — `server/async_persistence.py`
- **._process_exits_for_room()** (4 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- *... and 121 more nodes in this community*

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (27 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (21 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (11 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (8 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (6 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (6 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (6 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (5 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (5 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_room_loader.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 594 (91%)
- INFERRED: 59 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*