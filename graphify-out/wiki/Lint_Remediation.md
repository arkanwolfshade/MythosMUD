# Lint Remediation

> 15 nodes

## Key Concepts

- **_apply_path_based_markers()** (6 connections) — `server/tests/conftest.py`
- **pytest_asyncio_loop_factories()** (6 connections) — `server/tests/conftest.py`
- **pytest_collection_modifyitems()** (5 connections) — `server/tests/conftest.py`
- **_create_test_event_loop()** (4 connections) — `server/tests/conftest.py`
- **_set_xdist_loadgroup_nodeid()** (4 connections) — `server/tests/conftest.py`
- **Item** (4 connections)
- **_test_file_in_category()** (3 connections) — `server/tests/conftest.py`
- **Config** (2 connections)
- **AbstractEventLoop** (2 connections)
- **Create an event loop suitable for MythosMUD tests. CRITICAL: On Windows,…** (1 connections) — `server/tests/conftest.py`
- **Register platform-appropriate loop factories for pytest-asyncio (Python 3.14+…** (1 connections) — `server/tests/conftest.py`
- **True when the collected test file lives under a unit/integration/e2e directory.** (1 connections) — `server/tests/conftest.py`
- **Append @group to pytest Item nodeid for xdist --dist loadgroup scheduling.…** (1 connections) — `server/tests/conftest.py`
- **Apply unit/integration/e2e markers (and xdist grouping) from the test file path.** (1 connections) — `server/tests/conftest.py`
- **Auto-mark tests based on their file path. Tests in unit/ get @pytest.mark.unit…** (1 connections) — `server/tests/conftest.py`

## Relationships

- [MythosMUD Database Placement](MythosMUD_Database_Placement.md) (6 shared connections)

## Source Files

- `server/tests/conftest.py`

## Audit Trail

- EXTRACTED: 23 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*