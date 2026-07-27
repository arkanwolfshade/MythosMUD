# Room Subscription Helpers

> 21 nodes · cohesion 0.10

## Key Concepts

- **get_async_session()** (53 connections) — `server/database.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **async_persistence_room_loader.py** (9 connections) — `server/async_persistence_room_loader.py`
- **fetch_professions()** (7 connections) — `server/async_persistence_direct_queries.py`
- **fetch_user_by_username_case_insensitive()** (7 connections) — `server/async_persistence_direct_queries.py`
- **main()** (5 connections) — `scripts/verify_and_load_seed.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.get_user_by_username_case_insensitive()** (4 connections) — `server/async_persistence.py`
- **Any** (4 connections) — `server/services/npc_combat_lucidity.py`
- **add_flavor_text_column.py** (3 connections) — `scripts/add_flavor_text_column.py`
- **add_flavor_text_column()** (3 connections) — `scripts/add_flavor_text_column.py`
- **Add flavor_text column if missing.** (1 connections) — `scripts/add_flavor_text_column.py`
- **Load seed data and verify.** (1 connections) — `scripts/verify_and_load_seed.py`
- **Direct async SQL queries used by AsyncPersistenceLayer.  Extracted to keep async** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get a user by username (case-insensitive).      MULTI-CHARACTER: Usernames are s** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get a user by username (case-insensitive).          MULTI-CHARACTER: Usernames a** (1 connections) — `server/async_persistence.py`
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence.py`
- **Room cache loading for async persistence layer.  Extracted from async_persistenc** (1 connections) — `server/async_persistence_room_loader.py`
- **Get an async database session as an async context manager.      Usage:         a** (1 connections) — `server/database.py`

## Relationships

- [NPC Admin API](NPC_Admin_API.md) (8 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (2 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (1 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (1 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/services/npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 125 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*