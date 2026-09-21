# AppConfig

> 92 nodes

## Key Concepts

- **AppConfig** (35 connections) — `server/config/models/app.py`
- **server/config/__init__.py** (29 connections) — `server/config/__init__.py`
- **test_config_init.py** (19 connections) — `server/tests/unit/config/test_config_init.py`
- **npc_combat_grace.py** (15 connections) — `server/services/npc_combat_grace.py`
- **.connection_manager()** (13 connections) — `server/services/combat_messaging/base.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_npc_combat_grace.py** (9 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **._sanitize_environment_for_nested_configs()** (8 connections) — `server/config/models/app.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **test_first_cors_origins_env_returns_first_match()** (6 connections) — `server/tests/unit/config/test_config_init.py`
- **MonkeyPatch** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **._first_cors_origins_env()** (5 connections) — `server/config/models/app.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **test_first_cors_origins_env_none_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_converts_comma_separated()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_already_json()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_only_commas()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- *... and 67 more nodes in this community*

## Relationships

- [get_config](get_config.md) (19 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (10 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [test_config_models.py](test_config_models.py.md) (3 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (3 shared connections)
- [LoggingConfig](LoggingConfig.md) (2 shared connections)
- [server/tests/conftest.py](server-tests-conftest.py.md) (2 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/services/test_npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 186 (87%)
- INFERRED: 28 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*