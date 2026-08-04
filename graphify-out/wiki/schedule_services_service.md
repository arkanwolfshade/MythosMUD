# schedule services service

> 43 nodes

## Key Concepts

- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **Any** (9 connections)
- **.__init__()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_entered()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.get_room_state_event()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_xp_awarded()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_updated()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_died()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_decay()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_delirium_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **player_state_event_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **Handles all player-related real-time events.** (1 connections) — `server/realtime/player_event_handlers.py`
- **Initialize the player event handler.          Args:             connection_manag** (1 connections) — `server/realtime/player_event_handlers.py`
- **Initialize utility functions and specialized handlers.** (1 connections) — `server/realtime/player_event_handlers.py`
- *... and 18 more nodes in this community*

## Relationships

- [combat services messaging](combat_services_messaging.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (5 shared connections)
- [item models rationale](item_models_rationale.md) (5 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [player occupant processor](player_occupant_processor.md) (2 shared connections)
- [feature services flag](feature_services_flag.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 133 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*