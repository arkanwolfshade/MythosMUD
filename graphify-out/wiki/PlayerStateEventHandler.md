# PlayerStateEventHandler

> 14 nodes

## Key Concepts

- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **BoundLogger** (4 connections)
- **Player** (1 connections)
- **Initialize utility functions and specialized handlers.** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handles player state update events (XP, DP, death, decay).** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Initialize state event handler. Args: connection_manager: ConnectionManager…** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Handle player XP award events by sending updates to the client. Args: event:…** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Handle player DP decay events by sending decay notification to the client.…** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Load stats and display fields for a DP update, or fall back when player is…** (1 connections) — `server/realtime/player_event_handlers_state.py`

## Relationships

- [RealTimeEventHandler](RealTimeEventHandler.md) (5 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (5 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (3 shared connections)
- [test_player_event_handlers_state.py](test_player_event_handlers_state.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 48 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*