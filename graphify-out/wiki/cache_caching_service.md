# cache caching service

> 23 nodes

## Key Concepts

- **Any** (13 connections)
- **.get_all_professions()** (5 connections) — `server/caching/cache_service.py`
- **.get_room_sync()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.__init__()** (4 connections) — `server/caching/cache_service.py`
- **.get_profession_by_id()** (4 connections) — `server/caching/cache_service.py`
- **.preload_frequently_accessed_data()** (4 connections) — `server/caching/cache_service.py`
- **.get_room()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definitions()** (3 connections) — `server/caching/cache_service.py`
- **.get_npc_definition()** (3 connections) — `server/caching/cache_service.py`
- **.get_spawn_rules()** (3 connections) — `server/caching/cache_service.py`
- **.get_cache_stats()** (3 connections) — `server/caching/cache_service.py`
- **Get room data with caching.          Args:             room_id: The room ID** (1 connections) — `server/caching/cache_service.py`
- **Get room data with caching (synchronous version).          Args:             roo** (1 connections) — `server/caching/cache_service.py`
- **Initialize the NPC cache service.          Args:             npc_service: NPC se** (1 connections) — `server/caching/cache_service.py`
- **Get NPC definitions with caching.          Args:             session: Database s** (1 connections) — `server/caching/cache_service.py`
- **Get a specific NPC definition with caching.          Args:             session:** (1 connections) — `server/caching/cache_service.py`
- **Get NPC spawn rules with caching.          Args:             session: Database s** (1 connections) — `server/caching/cache_service.py`
- **Initialize the profession cache service.          Args:             persistence:** (1 connections) — `server/caching/cache_service.py`
- **Get all professions with caching.          Returns:             List of professi** (1 connections) — `server/caching/cache_service.py`
- **Get a specific profession by ID with caching.          Args:             profess** (1 connections) — `server/caching/cache_service.py`
- **Get statistics for all caches.          Returns:             Dictionary containi** (1 connections) — `server/caching/cache_service.py`
- **Preload frequently accessed data into caches.          This method loads commonl** (1 connections) — `server/caching/cache_service.py`

## Relationships

- [startup npc service](startup_npc_service.md) (4 shared connections)
- [uuid services npc](uuid_services_npc.md) (4 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (3 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (3 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (2 shared connections)

## Source Files

- `server/caching/cache_service.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*