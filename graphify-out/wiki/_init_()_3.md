# . init ()

> 53 nodes

## Key Concepts

- **ProfessionCacheService** (15 connections) — `server/caching/cache_service.py`
- **NPCCacheService** (14 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **_FakeNPCService** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_npc_cache()** (7 connections) — `scripts/bench_cache_npc.py`
- **bench_cache_professions.py** (7 connections) — `scripts/bench_cache_professions.py`
- **.__init__()** (7 connections) — `server/caching/cache_service.py`
- **bench_cache_npc.py** (6 connections) — `scripts/bench_cache_npc.py`
- **bench_profession_cache()** (6 connections) — `scripts/bench_cache_professions.py`
- **_FakePersistence** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `scripts/bench_cache_professions.py`
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (4 connections) — `scripts/bench_cache_npc.py`
- **Any** (4 connections)
- **.get_spawn_rules()** (4 connections) — `scripts/bench_cache_npc.py`
- **_get_empty_dict()** (4 connections) — `scripts/bench_cache_professions.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (4 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `scripts/bench_cache_npc.py`
- **Any** (3 connections)
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- *... and 28 more nodes in this community*

## Relationships

- [world](world.md) (10 shared connections)
- [chat send with room bundle()](chat_send_with_room_bundle%28%29.md) (4 shared connections)
- [conftest](conftest.md) (4 shared connections)
- [init](init.md) (3 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [get current tick()](get_current_tick%28%29.md) (2 shared connections)

## Source Files

- `scripts/bench_cache_npc.py`
- `scripts/bench_cache_professions.py`
- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 167 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*