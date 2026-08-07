# caching lru cache

> 45 nodes

## Key Concepts

- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **K** (7 connections)
- **.items()** (7 connections) — `server/caching/lru_cache.py`
- **.get()** (6 connections) — `server/caching/lru_cache.py`
- **.put()** (6 connections) — `server/caching/lru_cache.py`
- **.get_or_set()** (6 connections) — `server/caching/lru_cache.py`
- **V** (5 connections)
- **.get_stats()** (5 connections) — `server/caching/lru_cache.py`
- **.keys()** (5 connections) — `server/caching/lru_cache.py`
- **.get_cache()** (5 connections) — `server/caching/lru_cache.py`
- **.get_all_stats()** (5 connections) — `server/caching/lru_cache.py`
- **._evict_expired_entries()** (4 connections) — `server/caching/lru_cache.py`
- **Any** (4 connections)
- **.values()** (4 connections) — `server/caching/lru_cache.py`
- **.create_cache()** (4 connections) — `server/caching/lru_cache.py`
- **.delete()** (3 connections) — `server/caching/lru_cache.py`
- **.clear()** (3 connections) — `server/caching/lru_cache.py`
- **.size()** (3 connections) — `server/caching/lru_cache.py`
- **.__len__()** (3 connections) — `server/caching/lru_cache.py`
- **.__contains__()** (3 connections) — `server/caching/lru_cache.py`
- **.__repr__()** (3 connections) — `server/caching/lru_cache.py`
- **.clear_all_caches()** (3 connections) — `server/caching/lru_cache.py`
- **.__init__()** (2 connections) — `server/caching/lru_cache.py`
- **.is_full()** (2 connections) — `server/caching/lru_cache.py`
- **.get_cache_names()** (2 connections) — `server/caching/lru_cache.py`
- *... and 20 more nodes in this community*

## Relationships

- [admin commands setstat](admin_commands_setstat.md) (9 shared connections)
- [player left room](player_left_room.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [services lucidity repository](services_lucidity_repository.md) (1 shared connections)
- [message realtime messaging](message_realtime_messaging.md) (1 shared connections)
- [map layout useMapLayout](map_layout_useMapLayout.md) (1 shared connections)
- [container inventory display](container_inventory_display.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`

## Audit Trail

- EXTRACTED: 142 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*