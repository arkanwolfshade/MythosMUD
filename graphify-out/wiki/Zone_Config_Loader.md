# Zone Config Loader

> 255 nodes

## Key Concepts

- **Player** (200 connections) — `server/models/player.py`
- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **PlayerDeathService** (29 connections) — `server/services/player_death_service.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **player_death_service.py** (20 connections) — `server/services/player_death_service.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.get_dead_players()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **.get_mortally_wounded_players()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **BoundLogger** (4 connections)
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- *... and 230 more nodes in this community*

## Relationships

- [Application Config Settings](Application_Config_Settings.md) (30 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (22 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (12 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (11 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (10 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (10 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (9 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (9 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (9 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (7 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/player.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 824 (89%)
- INFERRED: 100 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*