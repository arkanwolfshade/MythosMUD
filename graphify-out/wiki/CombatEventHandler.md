# CombatEventHandler

> 46 nodes

## Key Concepts

- **login_user()** (34 connections) — `server/auth/endpoints.py`
- **LoginRequest** (21 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (18 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **asyncio** (11 connections)
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **_get_user_characters()** (6 connections) — `server/auth/endpoints.py`
- **test_login_user_player_no_profession_id()** (5 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_profession_lookup_error()** (5 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_profession_lookup_none()** (5 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_profession_lookup_success()** (5 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_authenticate_raises_exception()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_authenticate_returns_none()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_generic_exception()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_http_exception_re_raised()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_id_mismatch()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_invalid_credentials()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_no_email()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_not_found()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_shutdown_pending()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_success()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_with_characters()** (5 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **get_async_session** (5 connections)
- **asyncio** (4 connections)
- **CharacterInfo** (1 connections)
- **get_container** (1 connections)
- *... and 21 more nodes in this community*

## Relationships

- [test_combat_service_modules.py](test_combat_service_modules.py.md) (17 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [maps.py](maps.py.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [container_persistence.py](container_persistence.py.md) (1 shared connections)
- [FakeHallucinationService](FakeHallucinationService.md) (1 shared connections)
- [test_lint_raw_sql_in_python.py](test_lint_raw_sql_in_python.py.md) (1 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`

## Audit Trail

- EXTRACTED: 99 (85%)
- INFERRED: 18 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*