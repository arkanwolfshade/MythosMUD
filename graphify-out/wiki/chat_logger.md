# chat_logger

> 8 nodes

## Key Concepts

- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **reset_config_singleton()** (3 connections) — `server/tests/conftest.py`
- **Reset the configuration cache.      In test mode, this is a no-op since get_conf** (1 connections) — `server/config/__init__.py`
- **Reset config singleton before and after each test.      In test mode, get_config** (1 connections) — `server/tests/conftest.py`
- **Test that reset_config() clears global state.** (1 connections) — `server/tests/unit/config/test_config.py`
- **Test that reset_config() works in test mode.** (1 connections) — `server/tests/unit/config/test_config_init.py`

## Relationships

- [Archive Frd Random](Archive_Frd_Random.md) (2 shared connections)
- [ESLint Conftest Fixtures](ESLint_Conftest_Fixtures.md) (2 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (2 shared connections)
- [Realtime Maintenance Connection](Realtime_Maintenance_Connection.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)

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