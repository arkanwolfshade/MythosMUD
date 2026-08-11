# Pylint Unique Findings

> 132 nodes

## Key Concepts

- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **envelope.py** (28 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **get_next_sequence_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **Any** (7 connections)
- **UUID** (6 connections)
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **BoundLogger** (4 connections)
- *... and 107 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (32 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (11 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (10 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (10 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (8 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (7 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (5 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (4 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (4 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (4 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (4 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (4 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/envelope.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 531 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*