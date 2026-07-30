# Connection Manager

> 257 nodes

## Key Concepts

- **test_player_preferences_service.py** (59 connections) — `server/tests/unit/services/test_player_preferences_service.py`
- **Result** (52 connections) — `scripts/run_test_ci.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **list_invites()** (10 connections) — `server/auth/endpoints.py`
- **InviteRead** (10 connections) — `server/schemas/auth/invite.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- **test_register_user_duplicate_username()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_integrity_error()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_no_email()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_id_mismatch()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- *... and 232 more nodes in this community*

## Relationships

- [metrics](metrics.md) (46 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (24 shared connections)
- [.use invite()](use_invite%28%29.md) (9 shared connections)
- [test security headers](test_security_headers.md) (7 shared connections)
- [equipment helpers](equipment_helpers.md) (7 shared connections)
- [test player preferences service](test_player_preferences_service.md) (7 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (6 shared connections)
- [real time](real_time.md) (5 shared connections)
- [.shutdown()](shutdown%28%29.md) (4 shared connections)
- [init](init.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [create access token()](create_access_token%28%29.md) (2 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/token_epoch.py`
- `server/schemas/auth/invite.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 867 (86%)
- INFERRED: 136 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*