# schedule services service

> 29 nodes

## Key Concepts

- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **Any** (9 connections)
- **.__init__()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_entered()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.get_room_state_event()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_xp_awarded()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_updated()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_died()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_decay()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_delirium_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handler()** (3 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **Handles all player-related real-time events.** (1 connections) — `server/realtime/player_event_handlers.py`
- **Initialize the player event handler.          Args:             connection_manag** (1 connections) — `server/realtime/player_event_handlers.py`
- **Initialize utility functions and specialized handlers.** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player entering a room with enhanced synchronization.          Args:** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player leaving a room with enhanced synchronization.          Args:** (1 connections) — `server/realtime/player_event_handlers.py`
- **Send occupants snapshot to a player.          CRITICAL: This method MUST include** (1 connections) — `server/realtime/player_event_handlers.py`
- **Build authoritative room_state event for a room (for request/response enter-room** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player XP award events by sending updates to the client.          Args:** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player DP update events by sending updates to the client.          Args:** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player death events by sending death notification to the client.** (1 connections) — `server/realtime/player_event_handlers.py`
- *... and 4 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [event bus events](event_bus_events.md) (3 shared connections)
- [commands communication channels](commands_communication_channels.md) (2 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)
- [message handler factory](message_handler_factory.md) (2 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (2 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [feature services flag](feature_services_flag.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [item models rationale](item_models_rationale.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`

## Audit Trail

- EXTRACTED: 91 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*