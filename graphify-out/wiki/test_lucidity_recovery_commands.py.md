# test_lucidity_recovery_commands.py

> 108 nodes · cohesion 0.03

## Key Concepts

- **ValueError** (345 connections)
- **process_room_files()** (9 connections) — `scripts/standardize_room_names.py`
- **field_validator** (8 connections)
- **standardize_room_names.py** (7 connections) — `scripts/standardize_room_names.py`
- **validate_codacy_coverage_gate.py** (7 connections) — `scripts/validate_codacy_coverage_gate.py`
- **validate_python_gate()** (7 connections) — `scripts/validate_codacy_coverage_gate.py`
- **cobertura_root_line_rate()** (6 connections) — `scripts/validate_codacy_coverage_gate.py`
- **Path** (6 connections)
- **validate_lcov_gate()** (6 connections) — `scripts/validate_codacy_coverage_gate.py`
- **load_room_file()** (5 connections) — `scripts/standardize_room_names.py`
- **save_room_file()** (5 connections) — `scripts/standardize_room_names.py`
- **cobertura_has_server_sources()** (5 connections) — `scripts/validate_codacy_coverage_gate.py`
- **_parse_cobertura_xml()** (5 connections) — `scripts/validate_codacy_coverage_gate.py`
- **.validate_direction()** (5 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (5 connections) — `server/models/command_exploration.py`
- **lcov_aggregate_hits()** (4 connections) — `scripts/validate_codacy_coverage_gate.py`
- **.validate_direction()** (4 connections) — `server/api/container_models.py`
- **.validate_invite_code()** (4 connections) — `server/auth/endpoints.py`
- **.validate_password()** (4 connections) — `server/auth/endpoints.py`
- **.validate_rate_limits()** (4 connections) — `server/config/models/chat_time.py`
- **.validate_compression_ratio()** (4 connections) — `server/config/models/chat_time.py`
- **.validate_combat_alert_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_performance_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_tick_interval()** (4 connections) — `server/config/models/game.py`
- *... and 83 more nodes in this community*

## Relationships

- [Room](Room.md) (19 shared connections)
- [test_look_item_helpers.py](test_look_item_helpers.py.md) (11 shared connections)
- [build_event](build_event.md) (11 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (8 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (7 shared connections)
- [get_username_from_user](get_username_from_user.md) (6 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (6 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (6 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (5 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)

## Source Files

- `scripts/standardize_room_names.py`
- `scripts/validate_codacy_coverage_gate.py`
- `server/api/container_models.py`
- `server/auth/endpoints.py`
- `server/config/models/chat_time.py`
- `server/config/models/game.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`
- `server/models/command_exploration.py`
- `server/models/command_inventory.py`
- `server/models/command_magic.py`
- `server/models/room.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 159 (32%)
- INFERRED: 343 (68%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*