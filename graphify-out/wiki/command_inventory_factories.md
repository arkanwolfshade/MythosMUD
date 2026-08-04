# command inventory factories

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

- [Exception Containers](Exception_Containers.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [profession game service](profession_game_service.md) (2 shared connections)
- [game models stats](game_models_stats.md) (2 shared connections)

## Source Files

- `server/api/professions.py`
- `server/tests/unit/api/test_professions_endpoints.py`

## Audit Trail

- EXTRACTED: 53 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*