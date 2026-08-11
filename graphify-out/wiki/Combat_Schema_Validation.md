# Combat Schema Validation

> 88 nodes

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (11 connections) — `server/npc_database.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (11 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (9 connections) — `server/npc_database.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **TestNPCSession** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEnsureNPCDatabaseDirectory** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **.test_get_npc_engine_raises_on_invalid_url()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_raises_on_none_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_disposes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestResetNPCDatabase** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_raises_for_non_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEventLoopHandling** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 63 more nodes in this community*

## Relationships

- [Spell Registry Costs](Spell_Registry_Costs.md) (22 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (3 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (3 shared connections)
- [Command Parser](Command_Parser.md) (2 shared connections)
- [Container Persistence Layer](Container_Persistence_Layer.md) (2 shared connections)

## Source Files

- `server/container/bundles/core.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 298 (93%)
- INFERRED: 21 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*