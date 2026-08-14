# Any

> 23 nodes

## Key Concepts

- **Any** (13 connections)
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.get_all_professions()** (3 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (3 connections) — `server/caching/cache_service.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (3 connections) — `server/caching/cache_service.py`
- **Initialize the room cache service. Args: persistence: Persistence layer instance** (1 connections) — `server/caching/cache_service.py`
- **Get room data with caching. Args: room_id: The room ID Returns: Room data…** (1 connections) — `server/caching/cache_service.py`
- **Get room data with caching (synchronous version). Args: room_id: The room ID…** (1 connections) — `server/caching/cache_service.py`
- **Initialize the NPC cache service. Args: npc_service: NPC service instance** (1 connections) — `server/caching/cache_service.py`
- **Get NPC definitions with caching. Args: session: Database session Returns: List…** (1 connections) — `server/caching/cache_service.py`
- **Get a specific NPC definition with caching. Args: session: Database session…** (1 connections) — `server/caching/cache_service.py`
- **Get NPC spawn rules with caching. Args: session: Database session Returns: List…** (1 connections) — `server/caching/cache_service.py`
- **Initialize the profession cache service. Args: persistence: Persistence layer…** (1 connections) — `server/caching/cache_service.py`
- **Get all professions with caching. Returns: List of profession objects** (1 connections) — `server/caching/cache_service.py`
- **Get a specific profession by ID with caching. Args: profession_id: The…** (1 connections) — `server/caching/cache_service.py`
- **Get statistics for all caches. Returns: Dictionary containing cache statistics** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [NPCCacheService](NPCCacheService.md) (4 shared connections)
- [get_cache_manager](get_cache_manager.md) (4 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (3 shared connections)
- [RoomCacheService](RoomCacheService.md) (3 shared connections)
- [CacheService](CacheService.md) (2 shared connections)

## Source Files

- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*