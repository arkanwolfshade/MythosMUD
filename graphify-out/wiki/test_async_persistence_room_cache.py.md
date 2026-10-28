# test_async_persistence_room_cache.py

> 7 nodes · cohesion 0.29

## Key Concepts

- **_AsyncPersistenceLike** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **_PlayerServiceLike** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_player_to_schema()** (3 connections) — `server/realtime/integration/game_state_provider.py`
- **Protocol** (2 connections)
- **Minimal duck-type for the app's PlayerService (issue #787: avoid Any at the…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert a Player model to its client-facing schema representation.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Minimal duck-type for the async persistence layer's player lookup.** (1 connections) — `server/realtime/integration/game_state_provider.py`

## Relationships

- [ChatLogger](ChatLogger.md) (2 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_game.py](test_game.py.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`

## Audit Trail

- EXTRACTED: 9 (90%)
- INFERRED: 1 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*