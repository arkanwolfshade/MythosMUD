# persistence rationale room

> 8 nodes

## Key Concepts

- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **test_update_player_connection_list_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_with_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_no_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Update player's connection list to only include active connections.      Args:** (1 connections) — `server/realtime/connection_establishment.py`
- **Test _update_player_connection_list() handles player not in player_websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() keeps active connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() removes player when no active connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [connection establishment realtime](connection_establishment_realtime.md) (4 shared connections)
- [player event state](player_event_state.md) (3 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*