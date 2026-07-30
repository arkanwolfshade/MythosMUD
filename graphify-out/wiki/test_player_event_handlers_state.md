# test player event handlers state

> 12 nodes

## Key Concepts

- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **get_all_professions()** (10 connections) — `server/api/professions.py`
- **get_profession_by_id()** (10 connections) — `server/api/professions.py`
- **_user()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_all_professions_requires_auth()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_profession_by_id_not_found()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_all_professions_success()** (3 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_profession_by_id_success()** (3 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **Request** (2 connections)
- **Retrieve all available professions for character creation with caching.      :pa** (1 connections) — `server/api/professions.py`
- **Retrieve specific profession details by ID with caching.      :param profession_** (1 connections) — `server/api/professions.py`
- **Unit tests for server.api.professions.** (1 connections) — `server/tests/unit/api/test_professions_endpoints.py`

## Relationships

- [admin shutdown command](admin_shutdown_command.md) (7 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (5 shared connections)
- [Connection Manager](Connection_Manager.md) (4 shared connections)
- [real time](real_time.md) (1 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)

## Source Files

- `server/api/professions.py`
- `server/tests/unit/api/test_professions_endpoints.py`

## Audit Trail

- EXTRACTED: 53 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*