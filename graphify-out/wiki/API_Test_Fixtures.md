# API Test Fixtures

> 94 nodes · cohesion 0.03

## Key Concepts

- **User** (184 connections) — `server/models/user.py`
- **test_auth_dependencies.py** (22 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_skills.py** (12 connections) — `server/tests/unit/api/test_skills.py`
- **conftest.py** (11 connections) — `server/tests/unit/api/conftest.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_current_superuser()** (10 connections) — `server/auth/dependencies.py`
- **test_user.py** (10 connections) — `server/tests/unit/models/test_user.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **SkillData** (5 connections) — `server/schemas/players/skill.py`
- **test_get_current_superuser_failure()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_success()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_with_none_user()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_failure()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_success()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_with_none_user()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_optional_current_user_with_user()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_generic_exception()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_logged_http_exception()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_db_connectivity_create_and_read_user()** (4 connections) — `server/tests/integration/test_db_connectivity.py`
- **User** (4 connections) — `server/auth/dependencies.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_skills.py`
- **test_get_skills_catalog_returns_list()** (3 connections) — `server/tests/unit/api/test_skills.py`
- **test_get_skills_catalog_unauthorized()** (3 connections) — `server/tests/unit/api/test_skills.py`
- *... and 69 more nodes in this community*

## Relationships

- [[Container Exception Handlers]] (28 shared connections)
- [[Argon2 Password Hashing]] (28 shared connections)
- [[NPC Admin API]] (25 shared connections)
- [[Container API Endpoints]] (17 shared connections)
- [[Restart Invalidating JWT]] (13 shared connections)
- [[Integration DB Fixtures]] (8 shared connections)
- [[Maps API Endpoints]] (8 shared connections)
- [[Game Status API]] (7 shared connections)
- [[Character Creation API]] (6 shared connections)
- [[SQLAlchemy Model Base]] (6 shared connections)
- [[Lucidity Database Models]] (4 shared connections)
- [[Container Loot Helpers]] (3 shared connections)

## Source Files

- `server/api/skills.py`
- `server/auth/dependencies.py`
- `server/models/user.py`
- `server/schemas/players/skill.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 395 (86%)
- INFERRED: 66 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
