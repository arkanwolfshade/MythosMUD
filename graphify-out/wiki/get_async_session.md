# get_async_session

> 25 nodes · cohesion 0.10

## Key Concepts

- **get_async_session()** (54 connections) — `server/database.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **fetch_professions()** (9 connections) — `server/async_persistence_direct_queries.py`
- **fetch_user_by_username_case_insensitive()** (9 connections) — `server/async_persistence_direct_queries.py`
- **async_persistence_room_loader.py** (9 connections) — `server/async_persistence_room_loader.py`
- **main()** (6 connections) — `scripts/verify_and_load_seed.py`
- **.apply_encounter_lucidity_effect()** (6 connections) — `server/services/npc_combat_lucidity.py`
- **verify_and_load_seed.py** (4 connections) — `scripts/verify_and_load_seed.py`
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.get_user_by_username_case_insensitive()** (4 connections) — `server/async_persistence.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **add_flavor_text_column.py** (3 connections) — `scripts/add_flavor_text_column.py`
- **add_flavor_text_column()** (3 connections) — `scripts/add_flavor_text_column.py`
- **Any** (2 connections)
- **Add flavor_text column if missing.** (1 connections) — `scripts/add_flavor_text_column.py`
- **Load seed data and verify.** (1 connections) — `scripts/verify_and_load_seed.py`
- **Direct async SQL queries used by AsyncPersistenceLayer.  Extracted to keep async** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get a user by username (case-insensitive).      MULTI-CHARACTER: Usernames are s** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get a user by username (case-insensitive).          MULTI-CHARACTER: Usernames a** (1 connections) — `server/async_persistence.py`
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence.py`
- **Room cache loading for async persistence layer.  Extracted from async_persistenc** (1 connections) — `server/async_persistence_room_loader.py`
- **Get an async database session as an async context manager.      Usage:         a** (1 connections) — `server/database.py`
- **Determine encounter category based on NPC definition metadata.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply lucidity loss when a player engages an eldritch entity.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`

## Relationships

- [.get_instance](get_instance.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)
- [User](User.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [exceptions.py](exceptions.py.md) (2 shared connections)
- [Profession](Profession.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (2 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/services/npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 137 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*