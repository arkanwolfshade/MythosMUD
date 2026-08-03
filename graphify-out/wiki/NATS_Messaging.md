# NATS Messaging

> 377 nodes

## Key Concepts

- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **test_player_event_handlers_respawn.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **PlayerRespawnedEvent** (20 connections) — `server/events/event_types.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (11 connections)
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **Any** (9 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 352 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (60 shared connections)
- [item models rationale](item_models_rationale.md) (17 shared connections)
- [Room Broadcast](Room_Broadcast.md) (12 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (12 shared connections)
- [look helpers commands](look_helpers_commands.md) (12 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (11 shared connections)
- [combat services messaging](combat_services_messaging.md) (10 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (9 shared connections)
- [services combat sync](services_combat_sync.md) (8 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (7 shared connections)
- [combat models rationale](combat_models_rationale.md) (6 shared connections)
- [models player rationale](models_player_rationale.md) (6 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/services/combat_hp_sync.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 1249 (95%)
- INFERRED: 68 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*