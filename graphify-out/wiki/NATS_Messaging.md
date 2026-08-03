# NATS Messaging

> 264 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_respawn.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerRespawnedEvent** (19 connections) — `server/events/event_types.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (11 connections)
- **Any** (9 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **.__init__()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Any** (7 connections)
- *... and 239 more nodes in this community*

## Relationships

- [item models rationale](item_models_rationale.md) (37 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (23 shared connections)
- [Room Broadcast](Room_Broadcast.md) (8 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (6 shared connections)
- [combat services messaging](combat_services_messaging.md) (6 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (6 shared connections)
- [models player rationale](models_player_rationale.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [player occupant processor](player_occupant_processor.md) (2 shared connections)
- [combat commands handler](combat_commands_handler.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 805 (96%)
- INFERRED: 32 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*