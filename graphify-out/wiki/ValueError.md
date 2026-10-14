# ValueError

> 95 nodes

## Key Concepts

- **ValueError** (345 connections)
- **field_validator** (8 connections)
- **fix_room_references()** (6 connections) — `scripts/fix_room_references.py`
- **.player_entered()** (6 connections) — `server/models/room.py`
- **UUID** (6 connections)
- **load_room_file()** (5 connections) — `scripts/fix_room_references.py`
- **save_room_file()** (5 connections) — `scripts/fix_room_references.py`
- **.player_left()** (5 connections) — `server/models/room.py`
- **.validate_name()** (5 connections) — `server/schemas/players/player_requests.py`
- **.validate_direction()** (4 connections) — `server/api/container_models.py`
- **.validate_invite_code()** (4 connections) — `server/auth/endpoints.py`
- **.validate_password()** (4 connections) — `server/auth/endpoints.py`
- **.validate_rate_limits()** (4 connections) — `server/config/models/chat_time.py`
- **.validate_compression_ratio()** (4 connections) — `server/config/models/chat_time.py`
- **.validate_combat_alert_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_performance_threshold()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_tick_interval()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_timeout()** (4 connections) — `server/config/models/game.py`
- **.validate_combat_xp_multiplier()** (4 connections) — `server/config/models/game.py`
- **.validate_grace_period_seconds()** (4 connections) — `server/config/models/game.py`
- **.validate_max_connections()** (4 connections) — `server/config/models/game.py`
- **.validate_derived_stats()** (4 connections) — `server/config/models/player_stats.py`
- **.validate_stat_range()** (4 connections) — `server/config/models/player_stats.py`
- **.validate_environment()** (4 connections) — `server/config/models/security_logging.py`
- *... and 70 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (18 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [test_optimized_security_validator.py](test_optimized_security_validator.py.md) (11 shared connections)
- [ContainerComponent](ContainerComponent.md) (10 shared connections)
- [Room](Room.md) (8 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (8 shared connections)
- [field_validator](field_validator.md) (7 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (6 shared connections)
- [.set_player_skills](set_player_skills.md) (5 shared connections)
- [endpoints.py](endpoints.py.md) (4 shared connections)
- [LoggingConfig](LoggingConfig.md) (4 shared connections)

## Source Files

- `scripts/fix_room_references.py`
- `server/api/container_models.py`
- `server/auth/endpoints.py`
- `server/config/models/chat_time.py`
- `server/config/models/game.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`
- `server/models/command_inventory.py`
- `server/models/room.py`
- `server/schemas/calendar/calendar.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 127 (27%)
- INFERRED: 345 (73%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*