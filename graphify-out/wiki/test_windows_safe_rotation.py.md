# test_windows_safe_rotation.py

> 83 nodes · cohesion 0.04

## Key Concepts

- **AppConfig** (35 connections) — `server/config/models/app.py`
- **server/config/__init__.py** (32 connections) — `server/config/__init__.py`
- **test_config_init.py** (19 connections) — `server/tests/unit/config/test_config_init.py`
- **npc_combat_grace.py** (15 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **test_npc_combat_grace.py** (9 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **._sanitize_environment_for_nested_configs()** (8 connections) — `server/config/models/app.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **load_motd()** (8 connections) — `server/utils/motd_loader.py`
- **test_motd_loader.py** (7 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **motd_loader.py** (7 connections) — `server/utils/motd_loader.py`
- **MonkeyPatch** (6 connections)
- **test_first_cors_origins_env_returns_first_match()** (6 connections) — `server/tests/unit/config/test_config_init.py`
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **._first_cors_origins_env()** (5 connections) — `server/config/models/app.py`
- **test_first_cors_origins_env_none_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_converts_comma_separated()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_already_json()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_only_commas()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **test_sanitize_environment_for_nested_configs_noop_when_unset()** (5 connections) — `server/tests/unit/config/test_config_init.py`
- **.__init__()** (3 connections) — `server/config/models/app.py`
- *... and 58 more nodes in this community*

## Relationships

- [Room](Room.md) (20 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (19 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [ChatLogger](ChatLogger.md) (5 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/services/npc_combat_grace.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/services/test_npc_combat_grace.py`
- `server/tests/unit/utils/test_motd_loader.py`
- `server/utils/motd_loader.py`

## Audit Trail

- EXTRACTED: 178 (91%)
- INFERRED: 18 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*