# Combat Schema Validation

> 72 nodes

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
- **TestCloseNpcDb** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_engine_raises_on_invalid_url()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_init_npc_db_raises_on_none_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_close_npc_db_disposes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestResetNPCDatabase** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **.test_get_npc_database_path_raises_for_non_postgresql()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEventLoopHandling** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **reset_state()** (3 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 47 more nodes in this community*

## Relationships

- [Command Parser Helpers](Command_Parser_Helpers.md) (19 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (7 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [Quality Audit Report](Quality_Audit_Report.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (3 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Coverage Disconnect Grace](Coverage_Disconnect_Grace.md) (3 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)

## Source Files

- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 262 (93%)
- INFERRED: 19 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*