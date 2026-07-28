# NPC Admin API

> 347 nodes · cohesion 0.01

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (75 connections) — `server/database.py`
- **test_database_helpers.py** (46 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **._initialize_database()** (17 connections) — `server/database.py`
- **get_database_path()** (16 connections) — `server/database_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **get_async_session()** (13 connections) — `server/database_helpers.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **init_db()** (11 connections) — `server/database.py`
- **set_test_database_url()** (10 connections) — `server/database_config_helpers.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **close_db()** (9 connections) — `server/database_helpers.py`
- **get_engine()** (9 connections) — `server/database_helpers.py`
- **get_session_maker()** (9 connections) — `server/database_helpers.py`
- **get_engine()** (8 connections) — `server/database.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- *... and 322 more nodes in this community*

## Relationships

- [Api Player Respawn](Api_Player_Respawn.md) (45 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (35 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (13 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (11 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (7 shared connections)
- [Invite Generate Invites](Invite_Generate_Invites.md) (6 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (5 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (4 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (4 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (4 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (3 shared connections)

## Source Files

- `scripts/load_seed_using_project_db.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/npc_database.py`
- `server/tests/unit/infrastructure/test_database.py`
- `server/tests/unit/infrastructure/test_database_error_handling.py`
- `server/tests/unit/infrastructure/test_database_extended.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/infrastructure/test_database_init.py`

## Audit Trail

- EXTRACTED: 1396 (96%)
- INFERRED: 60 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*