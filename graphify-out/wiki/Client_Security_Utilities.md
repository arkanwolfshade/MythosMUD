# Client Security Utilities

> 120 nodes

## Key Concepts

- **AsyncPersistenceLayer** (185 connections) — `server/async_persistence.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **Any** (20 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (6 connections) — `server/async_persistence.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **_DatabaseLoadResult** (5 connections) — `server/services/schedule_service.py`
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
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.async_list_rooms()** (4 connections) — `server/async_persistence.py`
- *... and 95 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (23 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (21 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (12 shared connections)
- [Client ASCII Map API](Client_ASCII_Map_API.md) (9 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (8 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (6 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (5 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (5 shared connections)
- [Combat Messaging Base](Combat_Messaging_Base.md) (5 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (5 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (4 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/npc/combat_integration_base.py`
- `server/npc/npc_base.py`
- `server/services/schedule_service.py`
- `server/tests/unit/infrastructure/conftest.py`

## Audit Trail

- EXTRACTED: 485 (90%)
- INFERRED: 53 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*