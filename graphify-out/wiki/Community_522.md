# Community 522

> 33 nodes

## Key Concepts

- **ProfessionCacheService** (19 connections) — `server/caching/cache_service.py`
- **Any** (13 connections)
- **TestProfessionCacheService** (7 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.__init__()** (6 connections) — `server/caching/cache_service.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.__init__()** (3 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (3 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (3 connections) — `server/caching/cache_service.py`
- **.__init__()** (3 connections) — `server/caching/cache_service.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (3 connections) — `server/caching/cache_service.py`
- **.__init__()** (3 connections) — `server/caching/cache_service.py`
- **.test_get_profession_by_id_hit_and_miss()** (3 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.invalidate_professions()** (2 connections) — `server/caching/cache_service.py`
- **.test_get_all_professions_hit_and_miss()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **.test_invalidate_professions()** (2 connections) — `server/tests/unit/caching/test_cache_service.py`
- **Initialize the room cache service. Args: persistence: Persistence layer instance** (2 connections) — `server/caching/cache_service.py`
- **Get room data with caching. Args: room_id: The room ID Returns: Room data…** (1 connections) — `server/caching/cache_service.py`
- **Get room data with caching (synchronous version). Args: room_id: The room ID…** (1 connections) — `server/caching/cache_service.py`
- **Initialize the NPC cache service. Args: npc_service: NPC service instance** (1 connections) — `server/caching/cache_service.py`
- **Get NPC definitions with caching. Args: session: Database session Returns: List…** (1 connections) — `server/caching/cache_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [Community 750](Community_750.md) (5 shared connections)
- [Community 695](Community_695.md) (5 shared connections)
- [Community 896](Community_896.md) (5 shared connections)
- [Community 88](Community_88.md) (4 shared connections)
- [Community 869](Community_869.md) (4 shared connections)
- [Community 1216](Community_1216.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/container/bundles/game.py`
- `server/tests/unit/caching/test_cache_service.py`

## Audit Trail

- EXTRACTED: 64 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*