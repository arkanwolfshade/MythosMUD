# Common Troubleshooting Guide

> 17 nodes · cohesion 0.15

## Key Concepts

- **conftest.py** (15 connections) — `server/tests/conftest.py`
- **_apply_path_based_markers()** (6 connections) — `server/tests/conftest.py`
- **pytest_collection_modifyitems()** (5 connections) — `server/tests/conftest.py`
- **Item** (4 connections)
- **_set_xdist_loadgroup_nodeid()** (4 connections) — `server/tests/conftest.py`
- **_test_file_in_category()** (3 connections) — `server/tests/conftest.py`
- **deterministic_random_seed()** (2 connections) — `server/tests/conftest.py`
- **ensure_test_environment_variables()** (2 connections) — `server/tests/conftest.py`
- **_get_db_name_from_url()** (2 connections) — `server/tests/conftest.py`
- **Test configuration and fixtures for MythosMUD greenfield test suite.  This modul** (1 connections) — `server/tests/conftest.py`
- **Set deterministic random seed for reproducible tests.** (1 connections) — `server/tests/conftest.py`
- **True when the collected test file lives under a unit/integration/e2e directory.** (1 connections) — `server/tests/conftest.py`
- **Append @group to pytest Item nodeid for xdist --dist loadgroup scheduling.** (1 connections) — `server/tests/conftest.py`
- **Apply unit/integration/e2e markers (and xdist grouping) from the test file path.** (1 connections) — `server/tests/conftest.py`
- **Auto-mark tests based on their file path.      Tests in unit/ get @pytest.mark.u** (1 connections) — `server/tests/conftest.py`
- **Extract database name from a PostgreSQL URL. Returns empty string on parse failu** (1 connections) — `server/tests/conftest.py`
- **Ensure critical environment variables are set before each test.      Some tests** (1 connections) — `server/tests/conftest.py`

## Relationships

- [ESLint Conftest Fixtures](ESLint_Conftest_Fixtures.md) (4 shared connections)
- [Fastapi Code Review](Fastapi_Code_Review.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Architecture Api Openapi](Architecture_Api_Openapi.md) (1 shared connections)

## Source Files

- `server/tests/conftest.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*