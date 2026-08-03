# channel broadcasting realtime

> 12 nodes

## Key Concepts

- **get_game_status()** (7 connections) — `server/api/game.py`
- **TestGetGameStatus** (5 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_game_status_success()** (4 connections) — `server/tests/unit/api/test_game.py`
- **TestGetGameStatusLogger** (4 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_game_status_empty_connections()** (3 connections) — `server/tests/unit/api/test_game.py`
- **.test_get_game_status_logs_debug()** (3 connections) — `server/tests/unit/api/test_game.py`
- **Get current game status and connection information.** (1 connections) — `server/api/game.py`
- **Test get_game_status endpoint.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_game_status returns game status data.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_game_status handles empty connections.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test logger calls in get_game_status.** (1 connections) — `server/tests/unit/api/test_game.py`
- **Test get_game_status logs debug messages.** (1 connections) — `server/tests/unit/api/test_game.py`

## Relationships

- [room realtime occupant](room_realtime_occupant.md) (3 shared connections)
- [invite models create](invite_models_create.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/api/game.py`
- `server/tests/unit/api/test_game.py`

## Audit Trail

- EXTRACTED: 29 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*