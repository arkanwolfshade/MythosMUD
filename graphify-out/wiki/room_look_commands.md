# room look commands

> 80 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **admin_teleport_utils.py** (14 connections) — `server/commands/admin_teleport_utils.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **BoundLogger** (4 connections)
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **test_build_event_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_sequence_priority()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **_get_next_global_sequence()** (3 connections) — `server/realtime/envelope.py`
- **_dp_posture_from_stats()** (3 connections) — `server/realtime/player_event_handlers_state.py`
- **test_uuid_encoder_handles_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_other_types()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_json_dumps()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 55 more nodes in this community*

## Relationships

- [combat services messaging](combat_services_messaging.md) (15 shared connections)
- [Room Broadcast](Room_Broadcast.md) (11 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (9 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (8 shared connections)
- [NPC Combat](NPC_Combat.md) (8 shared connections)
- [message handler factory](message_handler_factory.md) (7 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (5 shared connections)
- [item models rationale](item_models_rationale.md) (5 shared connections)
- [instance game manager](instance_game_manager.md) (4 shared connections)
- [combat configuration service](combat_configuration_service.md) (4 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (4 shared connections)
- [command models moderation](command_models_moderation.md) (4 shared connections)

## Source Files

- `server/commands/admin_teleport_utils.py`
- `server/realtime/envelope.py`
- `server/realtime/player_event_handlers_state.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 377 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*