# Components Ui Designtokens

> 10 nodes

## Key Concepts

- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **test_setup_player_and_room_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Get player and setup room subscription.      Args:         player_id: The player** (1 connections) — `server/realtime/connection_establishment.py`
- **Test _setup_player_and_room() successfully sets up player and room.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() returns False when player not found.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles no persistence.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles player with no room_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (5 shared connections)
- [Logging Structured Setup](Logging_Structured_Setup.md) (4 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*