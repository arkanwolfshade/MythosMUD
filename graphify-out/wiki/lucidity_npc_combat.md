# lucidity npc combat

> 85 nodes

## Key Concepts

- **connection_manager.py** (161 connections) — `server/realtime/connection_manager.py`
- **send_game_event()** (30 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (21 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_game_event()** (12 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_connection_message_impl()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **test_connection_manager_api.py** (10 connections) — `server/tests/unit/realtime/test_connection_manager_api.py`
- **__getattr__()** (9 connections) — `server/realtime/connection_manager.py`
- **send_room_event()** (8 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_global_event_impl()** (8 connections) — `server/realtime/connection_manager_methods.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_global_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (6 connections)
- **periodic_health_check_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **start_health_checks_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **convert_room_players_uuids_to_names_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_npcs_batch_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **get_room_occupants_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **handle_player_entered_room_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **handle_player_left_room_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- *... and 60 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (56 shared connections)
- [Error Conversion](Error_Conversion.md) (18 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (18 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (12 shared connections)
- [spell models rationale](spell_models_rationale.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (10 shared connections)
- [movement monitor game](movement_monitor_game.md) (9 shared connections)
- [container service services](container_service_services.md) (7 shared connections)
- [party service game](party_service_game.md) (6 shared connections)
- [connection realtime error](connection_realtime_error.md) (6 shared connections)
- [nats services service](nats_services_service.md) (6 shared connections)
- [combat services messaging](combat_services_messaging.md) (6 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_manager_utils.py`
- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_connection_manager_api.py`

## Audit Trail

- EXTRACTED: 444 (95%)
- INFERRED: 22 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*