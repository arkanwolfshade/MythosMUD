# build_event

> 81 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging/base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **HasConnectionManager** (6 connections) — `server/services/combat_messaging/base.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **.broadcast_player_death()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.broadcast_player_respawn()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.send_dp_decay_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._send_mortally_wounded_personal_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_sequence_priority()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_other_types()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **_get_next_global_sequence()** (3 connections) — `server/realtime/envelope.py`
- **._build_mortally_wounded_messages()** (3 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **test_build_event_all_parameters()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 56 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (18 shared connections)
- [CombatBroadcastMixin](CombatBroadcastMixin.md) (10 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (9 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (5 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (4 shared connections)
- [AttributeError](AttributeError.md) (4 shared connections)
- [CombatMessagingIntegration](CombatMessagingIntegration.md) (3 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (3 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (3 shared connections)
- [position_commands.py](position_commands.py.md) (3 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 251 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*