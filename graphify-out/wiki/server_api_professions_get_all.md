# server api professions get all

> 14 nodes

## Key Concepts

- **test_professions_endpoints.py** (15 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **get_all_professions()** (11 connections) — `server/api/professions.py`
- **get_profession_by_id()** (11 connections) — `server/api/professions.py`
- **test_get_all_professions_requires_auth()** (5 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_profession_by_id_not_found()** (5 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_all_professions_success()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_profession_by_id_success()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **_user()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **asyncio** (4 connections)
- **get** (2 connections)
- **Request** (2 connections)
- **Retrieve all available professions for character creation with caching. :param…** (1 connections) — `server/api/professions.py`
- **Retrieve specific profession details by ID with caching. :param profession_id:…** (1 connections) — `server/api/professions.py`
- **Unit tests for server.api.professions.** (1 connections) — `server/tests/unit/api/test_professions_endpoints.py`

## Relationships

- [server api players](server_api_players.md) (5 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (5 shared connections)
- [server api character creation](server_api_character_creation.md) (4 shared connections)
- [dependsparam](dependsparam.md) (4 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)

## Source Files

- `server/api/professions.py`
- `server/tests/unit/api/test_professions_endpoints.py`

## Audit Trail

- EXTRACTED: 42 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*