# Server Config Loading

> 43 nodes · cohesion 0.05

## Key Concepts

- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **__init__.py** (9 connections) — `server/config/__init__.py`
- **_create_config_instance()** (6 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **AppConfig** (4 connections) — `server/config/__init__.py`
- **test_get_config_fresh_instances_in_test_mode()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_test_mode_returns_fresh_instances()** (3 connections) — `server/tests/unit/config/test_config.py`
- **reset_config_singleton()** (3 connections) — `server/tests/conftest.py`
- **Configuration module for MythosMUD server.  This module provides type-safe, vali** (1 connections) — `server/config/__init__.py`
- **Reset the configuration cache.      In test mode, this is a no-op since get_conf** (1 connections) — `server/config/__init__.py`
- **Detect if running in test environment.      Uses multiple detection methods to r** (1 connections) — `server/config/__init__.py`
- *... and 18 more nodes in this community*

## Relationships

- [[NPC Admin API]] (19 shared connections)
- [[Application Config Settings]] (2 shared connections)
- [[ESLint Conftest Fixtures]] (2 shared connections)
- [[Look Command Helpers]] (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/tests/conftest.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`

## Audit Trail

- EXTRACTED: 120 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
