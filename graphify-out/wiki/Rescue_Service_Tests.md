# Rescue Service Tests

> 88 nodes · cohesion 0.04

## Key Concepts

- **PlayerLucidity** (73 connections) — `server/models/lucidity.py`
- **handle_ground_command()** (32 connections) — `server/commands/rescue_commands.py`
- **rescue_commands.py** (31 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **rescue_service.py** (16 connections) — `server/services/rescue_service.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **RescueService** (11 connections) — `server/services/rescue_service.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **Any** (7 connections)
- **.rescue()** (7 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **UUID** (5 connections)
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_target()** (4 connections) — `server/commands/rescue_commands.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **Any** (4 connections)
- **test_handle_ground_command_apply_lucidity_error()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 63 more nodes in this community*

## Relationships

- [Player Death Service Tests](Player_Death_Service_Tests.md) (15 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (14 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (14 shared connections)
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (11 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (10 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (5 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (4 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (4 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (4 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (3 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (3 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/models/lucidity.py`
- `server/services/rescue_service.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 351 (89%)
- INFERRED: 44 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*