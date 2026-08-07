# health service services

> 72 nodes

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **create_access_token()** (32 connections) — `server/auth_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_expired()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_wrong_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_jwt_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_attribute_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_custom_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_wrong_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_audience()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_expired_token_immediately()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **setup_jwt_secret()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_returns_false_on_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_success()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 47 more nodes in this community*

## Relationships

- [package argon2 engines](package_argon2_engines.md) (19 shared connections)
- [nats services metrics](nats_services_metrics.md) (18 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (10 shared connections)
- [command models moderation](command_models_moderation.md) (3 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [add used user](add_used_user.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 233 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*