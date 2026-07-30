# process dead players()

> 80 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
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
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **generate_invites.py** (4 connections) — `tools/invite_tools/generate_invites.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **.get_default_starting_room()** (3 connections) — `server/game/player_service.py`
- *... and 55 more nodes in this community*

## Relationships

- [world](world.md) (17 shared connections)
- [close db()](close_db%28%29.md) (11 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (5 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [PanelManager](PanelManager.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (3 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (3 shared connections)
- [add hashed password column](add_hashed_password_column.md) (2 shared connections)
- [init](init.md) (2 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (2 shared connections)
- [combat attack](combat_attack.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/game/player_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/conftest.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 337 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*