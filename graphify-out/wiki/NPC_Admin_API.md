# NPC Admin API

> 79 nodes · cohesion 0.01

## Key Concepts

- **database.py** (74 connections) — `server/database.py`
- **database_helpers.py** (30 connections) — `server/database_helpers.py`
- **DatabaseManager** (29 connections) — `server/database.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **reset_database()** (16 connections) — `server/database.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **get_database_path()** (15 connections) — `server/database_helpers.py`
- **get_database_path()** (12 connections) — `server/database.py`
- **get_async_session()** (12 connections) — `server/database_helpers.py`
- **AsyncSession** (11 connections) — `server/database_helpers.py`
- **init_db()** (11 connections) — `server/database.py`
- **async_sessionmaker** (10 connections) — `server/database_helpers.py`
- **AsyncEngine** (10 connections) — `server/database_helpers.py`
- **Path** (10 connections) — `server/database_helpers.py`
- **close_db()** (9 connections) — `server/database.py`
- **get_postgres_connect_args()** (9 connections) — `server/database_config_helpers.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **.get_instance()** (8 connections) — `server/database.py`
- **get_engine()** (8 connections) — `server/database.py`
- **close_db()** (8 connections) — `server/database_helpers.py`
- **get_engine()** (8 connections) — `server/database_helpers.py`
- **get_session_maker()** (8 connections) — `server/database_helpers.py`
- **init_db()** (8 connections) — `server/database_helpers.py`
- **reset_database()** (7 connections) — `server/database_helpers.py`
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- *... and 54 more nodes in this community*

## Relationships

- [Api Player Respawn](Api_Player_Respawn.md) (11 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (9 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (4 shared connections)
- [Invite Generate Invites](Invite_Generate_Invites.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (3 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (2 shared connections)

## Source Files

- `scripts/load_seed_using_project_db.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/npc_database.py`

## Audit Trail

- EXTRACTED: 438 (89%)
- INFERRED: 53 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*