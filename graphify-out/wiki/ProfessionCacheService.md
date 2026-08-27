# ProfessionCacheService

> 25 nodes

## Key Concepts

- **get_cached_player()** (15 connections) — `server/utils/player_cache.py`
- **cache_player()** (13 connections) — `server/utils/player_cache.py`
- **test_player_cache.py** (11 connections) — `server/tests/unit/utils/test_player_cache.py`
- **player_cache.py** (7 connections) — `server/utils/player_cache.py`
- **_get_request_state()** (6 connections) — `server/utils/player_cache.py`
- **test_cache_and_get_player()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_multiple()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_overwrite()** (4 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_cache_player_no_state()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_no_state()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_none()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **test_get_cached_player_nonexistent()** (3 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Any** (3 connections)
- **Unit tests for player_cache utilities. Tests the player caching functions for…** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test get_cached_player() returns None when no cache exists.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test cache_player() and get_cached_player() operations.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test get_cached_player() returns None for nonexistent key.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test cache_player() can cache multiple players.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test cache_player() overwrites existing entries.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test get_cached_player() handles missing state.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Test cache_player() handles missing state gracefully.** (1 connections) — `server/tests/unit/utils/test_player_cache.py`
- **Helpers for caching player objects during a single command request. This avoids…** (1 connections) — `server/utils/player_cache.py`
- **Safely extract the state object from a FastAPI/Starlette request.** (1 connections) — `server/utils/player_cache.py`
- **Return a cached player object for this request if one exists.** (1 connections) — `server/utils/player_cache.py`
- **Cache a player object on the request for reuse within the command.** (1 connections) — `server/utils/player_cache.py`

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (5 shared connections)
- [asyncio](asyncio.md) (5 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_player_cache.py`
- `server/utils/player_cache.py`

## Audit Trail

- EXTRACTED: 50 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*