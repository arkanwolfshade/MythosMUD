# Container Persistence Queries

> 52 nodes

## Key Concepts

- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **UUID** (4 connections)
- **test_start_grace_period_reconnection_cancels()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **test_rest_interrupts_combat_action()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_start_grace_period_creates_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_player_not_found()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **mock_app_with_services()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 27 more nodes in this community*

## Relationships

- [NATS Message Broker](NATS_Message_Broker.md) (9 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (9 shared connections)
- [API Type Guards](API_Type_Guards.md) (6 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (4 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (4 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (3 shared connections)
- [Look Player Command](Look_Player_Command.md) (3 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (3 shared connections)
- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (3 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (3 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 212 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*