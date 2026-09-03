# Async Persistence Direct Queries

> 23 nodes

## Key Concepts

- **get_async_session()** (55 connections) — `server/database.py`
- **async_persistence_direct_queries.py** (11 connections) — `server/async_persistence_direct_queries.py`
- **fetch_professions()** (6 connections) — `server/async_persistence_direct_queries.py`
- **fetch_user_by_username_case_insensitive()** (6 connections) — `server/async_persistence_direct_queries.py`
- **verify_and_load_seed.py** (5 connections) — `scripts/verify_and_load_seed.py`
- **main()** (4 connections) — `scripts/verify_and_load_seed.py`
- **.get_user_by_username_case_insensitive()** (4 connections) — `server/async_persistence.py`
- **add_flavor_text_column.py** (4 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_using_project_db.py** (4 connections) — `scripts/load_seed_using_project_db.py`
- **add_flavor_text_column()** (3 connections) — `scripts/add_flavor_text_column.py`
- **load_seed_data()** (3 connections) — `scripts/load_seed_using_project_db.py`
- **AsyncSession** (3 connections)
- **Profession** (1 connections)
- **User** (1 connections)
- **User** (1 connections)
- **Add flavor_text column if missing.** (1 connections) — `scripts/add_flavor_text_column.py`
- **Load all seed data files.** (1 connections) — `scripts/load_seed_using_project_db.py`
- **Load seed data and verify.** (1 connections) — `scripts/verify_and_load_seed.py`
- **Direct async SQL queries used by AsyncPersistenceLayer. Extracted to keep…** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get a user by username (case-insensitive). MULTI-CHARACTER: Usernames are…** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get a user by username (case-insensitive). MULTI-CHARACTER: Usernames are…** (1 connections) — `server/async_persistence.py`
- **Get an async database session as an async context manager. Usage: async for…** (1 connections) — `server/database.py`

## Relationships

- [Test Database Extended](Test_Database_Extended.md) (5 shared connections)
- [Database](Database.md) (5 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (4 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (4 shared connections)
- [Test Rescue Commands](Test_Rescue_Commands.md) (3 shared connections)
- [Test Config Init](Test_Config_Init.md) (2 shared connections)
- [Async Persistence](Async_Persistence.md) (2 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (2 shared connections)
- [Async Persistence Room Loader](Async_Persistence_Room_Loader.md) (2 shared connections)
- [Catatonia Check](Catatonia_Check.md) (2 shared connections)
- [Test Admin Setlucidity Command](Test_Admin_Setlucidity_Command.md) (2 shared connections)
- [Test Channel Commands](Test_Channel_Commands.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/database.py`

## Audit Trail

- EXTRACTED: 91 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*