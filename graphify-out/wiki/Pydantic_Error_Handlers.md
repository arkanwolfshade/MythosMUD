# Pydantic Error Handlers

> 209 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_respawn.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **Any** (7 connections)
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **UUID** (6 connections)
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **.process_dict_occupant()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- **BoundLogger** (4 connections)
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_xp_awarded()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.__init__()** (4 connections) — `server/realtime/player_event_handlers_utils.py`
- *... and 184 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (36 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (13 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (11 shared connections)
- [Test Value Distribution](Test_Value_Distribution.md) (5 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [Archive Lucidity System](Archive_Lucidity_System.md) (2 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 570 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*