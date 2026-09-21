# _AsyncPersistenceLike

> 7 nodes

## Key Concepts

- **_AsyncPersistenceLike** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **_PlayerServiceLike** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_player_to_schema()** (3 connections) — `server/realtime/integration/game_state_provider.py`
- **Protocol** (2 connections)
- **Minimal duck-type for the app's PlayerService (issue #787: avoid Any at the…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert a Player model to its client-facing schema representation.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Minimal duck-type for the async persistence layer's player lookup.** (1 connections) — `server/realtime/integration/game_state_provider.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`

## Audit Trail

- EXTRACTED: 9 (90%)
- INFERRED: 1 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*