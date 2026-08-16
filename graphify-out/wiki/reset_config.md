# reset_config

> 32 nodes

## Key Concepts

- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
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
- **Reset the configuration cache. In test mode, this is a no-op since get_config()…** (1 connections) — `server/config/__init__.py`
- **Detect if running in test environment. Uses multiple detection methods to…** (1 connections) — `server/config/__init__.py`
- **Unit tests for config module initialization.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- **Test that get_config() returns fresh instances in test mode.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- **Test that reset_config() works in test mode.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- **Test that config has server configuration.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- **Test that config has database configuration.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- **Test that config has game configuration.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- **Test that get_config() returns an AppConfig object.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- *... and 7 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (15 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/tests/conftest.py](server-tests-conftest.py.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*