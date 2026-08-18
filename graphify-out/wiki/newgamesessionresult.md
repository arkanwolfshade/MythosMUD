# NewGameSessionResult

> 5 nodes

## Key Concepts

- **NewGameSessionResult** (7 connections) — `server/realtime/connection_session_management.py`
- **.handle_new_game_session()** (5 connections) — `server/realtime/connection_manager.py`
- **TypedDict** (1 connections)
- **Handle a new game session by disconnecting existing connections.** (1 connections) — `server/realtime/connection_manager.py`
- **Result payload from handle_new_game_session_impl.** (1 connections) — `server/realtime/connection_session_management.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_session_management.py`

## Audit Trail

- EXTRACTED: 10 (91%)
- INFERRED: 1 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*