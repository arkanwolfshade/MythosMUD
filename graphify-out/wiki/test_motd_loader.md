# test motd loader

> 8 nodes

## Key Concepts

- **.load_player_mutes_async()** (7 connections) — `server/services/user_manager.py`
- **.load_player_mutes_batch()** (6 connections) — `server/services/user_manager.py`
- **.is_player_muted_async()** (5 connections) — `server/services/user_manager.py`
- **._is_cache_valid()** (5 connections) — `server/services/user_manager.py`
- **Async version of is_player_muted using async mute loading.          Args:** (1 connections) — `server/services/user_manager.py`
- **Check if cached mute data is still valid.          Args:             player_i** (1 connections) — `server/services/user_manager.py`
- **Async version of load_player_mutes using asyncio.to_thread for file I/O.** (1 connections) — `server/services/user_manager.py`
- **Batch load mute data for multiple players concurrently.          Args:** (1 connections) — `server/services/user_manager.py`

## Relationships

- [UUID](UUID.md) (11 shared connections)

## Source Files

- `server/services/user_manager.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*