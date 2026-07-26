# reset_config

> 8 nodes · cohesion 0.25

## Key Concepts

- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **reset_config_singleton()** (3 connections) — `server/tests/conftest.py`
- **Reset the configuration cache.      In test mode, this is a no-op since get_conf** (1 connections) — `server/config/__init__.py`
- **Reset config singleton before and after each test.      In test mode, get_config** (1 connections) — `server/tests/conftest.py`
- **Test that reset_config() works in test mode.** (1 connections) — `server/tests/unit/config/test_config_init.py`
- **Test that reset_config() clears global state.** (1 connections) — `server/tests/unit/config/test_config.py`

## Relationships

- [AppConfig](AppConfig.md) (2 shared connections)
- [conftest.py](conftest.py.md) (2 shared connections)
- [test_config.py](test_config.py.md) (2 shared connections)
- [test_config_init.py](test_config_init.py.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/tests/conftest.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*