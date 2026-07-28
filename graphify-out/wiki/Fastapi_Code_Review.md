# Fastapi Code Review

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

- [Application Config Settings](Application_Config_Settings.md) (2 shared connections)
- [Common Troubleshooting Guide](Common_Troubleshooting_Guide.md) (2 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (2 shared connections)
- [Realtime Connection State](Realtime_Connection_State.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)

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