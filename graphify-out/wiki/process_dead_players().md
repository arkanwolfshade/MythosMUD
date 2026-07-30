# process dead players()

> 64 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **reset_config_singleton()** (3 connections) — `server/tests/conftest.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_test_mode_returns_fresh_instances()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- *... and 39 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (21 shared connections)
- [world](world.md) (11 shared connections)
- [eslint.config](eslint.config.md) (2 shared connections)
- [.get lucidity service()](get_lucidity_service%28%29.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [BaseUserManager](BaseUserManager.md) (2 shared connections)
- [add hashed password column](add_hashed_password_column.md) (1 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/tests/conftest.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`

## Audit Trail

- EXTRACTED: 197 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*