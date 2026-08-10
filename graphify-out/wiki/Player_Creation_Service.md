# Player Creation Service

> 267 nodes

## Key Concepts

- **Player** (200 connections) — `server/models/player.py`
- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **PlayerDeathService** (29 connections) — `server/services/player_death_service.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **player_death_service.py** (20 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **.handle_player_death()** (10 connections) — `server/services/player_death_service.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **.process_mortally_wounded_tick()** (7 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **test_health_repository_cold_resistance.py** (7 connections) — `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.get_dead_players()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.get_mortally_wounded_players()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- *... and 242 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (21 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (12 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (12 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (11 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (10 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (10 shared connections)
- [Container Data Models](Container_Data_Models.md) (10 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (10 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (6 shared connections)
- [Dependency Upgrade Report](Dependency_Upgrade_Report.md) (6 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (6 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (6 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/player.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/persistence/test_health_repository_cold_resistance.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 820 (89%)
- INFERRED: 103 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*