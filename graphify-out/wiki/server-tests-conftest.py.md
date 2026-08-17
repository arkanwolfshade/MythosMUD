# server/tests/conftest.py

> 33 nodes

## Key Concepts

- **server/tests/conftest.py** (17 connections) — `server/tests/conftest.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **_apply_path_based_markers()** (6 connections) — `server/tests/conftest.py`
- **pytest_asyncio_loop_factories()** (6 connections) — `server/tests/conftest.py`
- **pytest_collection_modifyitems()** (5 connections) — `server/tests/conftest.py`
- **test_logger()** (5 connections) — `server/tests/conftest.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **_create_test_event_loop()** (4 connections) — `server/tests/conftest.py`
- **reset_config_singleton()** (4 connections) — `server/tests/conftest.py`
- **_set_xdist_loadgroup_nodeid()** (4 connections) — `server/tests/conftest.py`
- **Item** (4 connections)
- **fixture** (4 connections)
- **deterministic_random_seed()** (3 connections) — `server/tests/conftest.py`
- **ensure_test_environment_variables()** (3 connections) — `server/tests/conftest.py`
- **_test_file_in_category()** (3 connections) — `server/tests/conftest.py`
- **_get_db_name_from_url()** (2 connections) — `server/tests/conftest.py`
- **Config** (2 connections)
- **AbstractEventLoop** (2 connections)
- **BoundLogger** (1 connections)
- **Reset the configuration cache. In test mode, this is a no-op since get_config()…** (1 connections) — `server/config/__init__.py`
- **Detect if running in test environment. Uses multiple detection methods to…** (1 connections) — `server/config/__init__.py`
- **Test configuration and fixtures for MythosMUD greenfield test suite. This…** (1 connections) — `server/tests/conftest.py`
- **Reset config singleton before and after each test. In test mode, get_config()…** (1 connections) — `server/tests/conftest.py`
- **Set deterministic random seed for reproducible tests.** (1 connections) — `server/tests/conftest.py`
- **Create an event loop suitable for MythosMUD tests. CRITICAL: On Windows,…** (1 connections) — `server/tests/conftest.py`
- *... and 8 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [get_config](get_config.md) (5 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/tests/conftest.py`

## Audit Trail

- EXTRACTED: 56 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*