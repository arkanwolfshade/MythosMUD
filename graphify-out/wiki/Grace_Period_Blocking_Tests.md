# Grace Period Blocking Tests

> 67 nodes

## Key Concepts

- **RoomCacheService** (17 connections) — `server/caching/cache_service.py`
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **ProfessionCacheService** (15 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **__init__.py** (12 connections) — `server/caching/__init__.py`
- **CacheService** (8 connections) — `server/caching/cache_service.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **bench_cache.py** (6 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (6 connections) — `scripts/bench_cache.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **bench_room_cache()** (5 connections) — `scripts/bench_cache.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `scripts/bench_cache_professions.py`
- **cached()** (5 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (4 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **Any** (3 connections)
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- *... and 42 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Alias Command Models](Alias_Command_Models.md) (6 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (6 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (2 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (2 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (1 shared connections)

## Source Files

- `scripts/bench_cache.py`
- `scripts/bench_cache_professions.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 217 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*