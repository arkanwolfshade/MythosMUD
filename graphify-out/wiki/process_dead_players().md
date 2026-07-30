# process dead players()

> 47 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **generate_invites.py** (4 connections) — `tools/invite_tools/generate_invites.py`
- **reset_config_singleton()** (3 connections) — `server/tests/conftest.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_test_mode_returns_fresh_instances()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_fresh_instances_in_test_mode()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_config_smoke.py** (3 connections) — `server/tests/unit/test_config_smoke.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/test_config_smoke.py`
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites.py`
- **main()** (3 connections) — `tools/invite_tools/generate_invites.py`
- **Detect if running in test environment.      Uses multiple detection methods to r** (1 connections) — `server/config/__init__.py`
- *... and 22 more nodes in this community*

## Relationships

- [Any](Any.md) (11 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (7 shared connections)
- [real time](real_time.md) (5 shared connections)
- [Player](Player.md) (5 shared connections)
- [world](world.md) (4 shared connections)
- [test security headers](test_security_headers.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [.model dump()](model_dump%28%29.md) (3 shared connections)
- [process all status effects()](process_all_status_effects%28%29.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (2 shared connections)
- [combat attack](combat_attack.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/tests/conftest.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 221 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*