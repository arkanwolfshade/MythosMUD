# Player Event Handlers

> 37 nodes

## Key Concepts

- **PlayerEventHandler** (21 connections) — `server/realtime/player_event_handlers.py`
- **.__init__()** (9 connections) — `server/realtime/player_event_handlers.py`
- **._initialize_modules()** (7 connections) — `server/realtime/event_handler.py`
- **._initialize_handlers()** (5 connections) — `server/realtime/player_event_handlers.py`
- **.get_room_state_event()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_entered()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_delirium_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_died()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_decay()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_updated()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_xp_awarded()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/player_event_handlers.py`
- **UUID** (3 connections)
- **MessageBuilder** (2 connections)
- **OccupantsUpdateFn** (2 connections)
- **PlayerNameExtractor** (2 connections)
- **RoomOccupantManager** (2 connections)
- **ChatLogger** (1 connections)
- **JsonMap** (1 connections)
- **RoomSyncService** (1 connections)
- **ConnectionManager** (1 connections)
- **Initialize specialized handler modules.** (1 connections) — `server/realtime/event_handler.py`
- **Handle player entering a room with enhanced synchronization. Args: event: The…** (1 connections) — `server/realtime/player_event_handlers.py`
- *... and 12 more nodes in this community*

## Relationships

- [Test Event Handler](Test_Event_Handler.md) (6 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (6 shared connections)
- [Test Player Event Handlers](Test_Player_Event_Handlers.md) (2 shared connections)
- [Test Player Event Handlers Respawn](Test_Player_Event_Handlers_Respawn.md) (2 shared connections)
- [Combat Events](Combat_Events.md) (2 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`

## Audit Trail

- EXTRACTED: 55 (89%)
- INFERRED: 7 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*