# MythosMUD Database Placement

> 30 nodes

## Key Concepts

- **server/tests/conftest.py** (17 connections) — `server/tests/conftest.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **reset_config()** (7 connections) — `server/config/__init__.py`
- **test_logger()** (5 connections) — `server/tests/conftest.py`
- **reset_config_singleton()** (4 connections) — `server/tests/conftest.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **fixture** (4 connections)
- **deterministic_random_seed()** (3 connections) — `server/tests/conftest.py`
- **ensure_test_environment_variables()** (3 connections) — `server/tests/conftest.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_test_mode_returns_fresh_instances()** (3 connections) — `server/tests/unit/config/test_config.py`
- **_get_db_name_from_url()** (2 connections) — `server/tests/conftest.py`
- **BoundLogger** (1 connections)
- **Reset the configuration cache. In test mode, this is a no-op since get_config()…** (1 connections) — `server/config/__init__.py`
- **Test configuration and fixtures for MythosMUD greenfield test suite. This…** (1 connections) — `server/tests/conftest.py`
- **Reset config singleton before and after each test. In test mode, get_config()…** (1 connections) — `server/tests/conftest.py`
- **Set deterministic random seed for reproducible tests.** (1 connections) — `server/tests/conftest.py`
- **Provide a logger for tests.** (1 connections) — `server/tests/conftest.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse…** (1 connections) — `server/tests/conftest.py`
- **Ensure critical environment variables are set before each test. Some tests may…** (1 connections) — `server/tests/conftest.py`
- **Unit tests for configuration system.** (1 connections) — `server/tests/unit/config/test_config.py`
- **Test that get_config() returns fresh instances in test mode.** (1 connections) — `server/tests/unit/config/test_config.py`
- *... and 5 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (12 shared connections)
- [Lint Remediation](Lint_Remediation.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/tests/conftest.py`
- `server/tests/unit/config/test_config.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*