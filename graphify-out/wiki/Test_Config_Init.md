# Test Config Init

> 84 nodes

## Key Concepts

- **get_config()** (92 connections) — `server/config/__init__.py`
- **test_config_init.py** (20 connections) — `server/tests/unit/config/test_config_init.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **._sanitize_environment_for_nested_configs()** (8 connections) — `server/config/models/app.py`
- **reset_config()** (7 connections) — `server/config/__init__.py`
- **test_first_cors_origins_env_returns_first_match()** (6 connections) — `server/tests/unit/config/test_config_init.py`
- **MonkeyPatch** (6 connections)
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **._first_cors_origins_env()** (5 connections) — `server/config/models/app.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **test_first_cors_origins_env_none_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_converts_comma_separated()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_already_json()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_only_commas()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **generate_invites.py** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **.__init__()** (4 connections) — `server/services/combat_configuration_service.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **.get_default_starting_room()** (3 connections) — `server/game/player_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_configuration_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_monitoring_service.py`
- *... and 59 more nodes in this community*

## Relationships

- [Cors](Cors.md) (21 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (3 shared connections)
- [Combat Integration Base](Combat_Integration_Base.md) (3 shared connections)
- [Test Combat Monitoring Service](Test_Combat_Monitoring_Service.md) (3 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (3 shared connections)
- [Test Combat Configuration Service](Test_Combat_Configuration_Service.md) (3 shared connections)
- [Test Feature Flag Service](Test_Feature_Flag_Service.md) (3 shared connections)
- [Time Service](Time_Service.md) (3 shared connections)
- [Npc Combat Grace](Npc_Combat_Grace.md) (2 shared connections)
- [Async Persistence Direct Queries](Async_Persistence_Direct_Queries.md) (2 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/game/player_service.py`
- `server/services/combat_configuration_service.py`
- `server/services/combat_monitoring_service.py`
- `server/services/feature_flag_service.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `server/time/time_service.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 201 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*