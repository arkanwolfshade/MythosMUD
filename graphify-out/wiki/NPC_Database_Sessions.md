# NPC Database Sessions

> 106 nodes · cohesion 0.03

## Key Concepts

- **npc_database.py** (27 connections) — `server/npc_database.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **npc_instance_service.py** (24 connections) — `server/services/npc_instance_service.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **instance.py** (22 connections) — `server/commands/npc_admin/instance.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **migrate_combat_data.py** (13 connections) — `server/scripts/migrate_combat_data.py`
- **get_npc_database_path()** (10 connections) — `server/npc_database.py`
- **init_npc_db()** (10 connections) — `server/npc_database.py`
- **_initialize_npc_database()** (10 connections) — `server/npc_database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **get_npc_session_maker()** (9 connections) — `server/npc_database.py`
- **TestNPCDatabaseInitialization** (8 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestCloseNpcDb** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSession** (6 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **ensure_npc_database_directory()** (6 connections) — `server/npc_database.py`
- **TestEnsureNPCDatabaseDirectory** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestGetNPCDatabasePath** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestInitNpcDb** (5 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **_parse_npc_spawn_args()** (5 connections) — `server/commands/npc_admin/instance.py`
- **reset_npc_database()** (5 connections) — `server/npc_database.py`
- **.test_close_npc_db_disposes_engine()** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestEventLoopHandling** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **TestNPCSessionMaker** (4 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- *... and 81 more nodes in this community*

## Relationships

- [[NPC Admin API]] (44 shared connections)
- [[Commands Npc Admin]] (9 shared connections)
- [[NPC Occupant Verification]] (8 shared connections)
- [[Migrate Combat]] (5 shared connections)
- [[NPC Services Bundle]] (5 shared connections)
- [[Alias Expansion Logic]] (4 shared connections)
- [[Combat Schema Validation]] (4 shared connections)
- [[Lifespan Startup Hooks]] (4 shared connections)
- [[Database Helper Tests]] (3 shared connections)
- [[NPC Definition Schemas]] (3 shared connections)
- [[NPC Definition Admin API]] (3 shared connections)
- [[Database Error Handling]] (2 shared connections)

## Source Files

- `server/commands/npc_admin/instance.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/npc_database.py`
- `server/scripts/migrate_combat_data.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 401 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
