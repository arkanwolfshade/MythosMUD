# get_npc_instance_service

> 100 nodes

## Key Concepts

- **test_auth_utils.py** (53 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **AuthenticationError** (32 connections) — `server/exceptions.py`
- **create_access_token()** (30 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **hash_password()** (16 connections) — `server/auth_utils.py`
- **auth_utils.py** (13 connections) — `server/auth_utils.py`
- **verify_password()** (8 connections) — `server/auth_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_jwt_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_audience()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_expired()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_custom_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_expired_token_immediately()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_wrong_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_wrong_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 75 more nodes in this community*

## Relationships

- [UserManager](UserManager.md) (8 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (6 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (4 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [properties](properties.md) (1 shared connections)
- [submitAuth.ts](submitAuth.ts.md) (1 shared connections)
- [security.ts](security.ts.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [Optimization Strategy Overview](Optimization_Strategy_Overview.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 195 (90%)
- INFERRED: 22 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*