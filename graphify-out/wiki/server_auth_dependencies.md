# server auth dependencies

> 125 nodes

## Key Concepts

- **Invite** (52 connections) — `server/models/invite.py`
- **InviteManager** (32 connections) — `server/auth/invites.py`
- **test_auth_dependencies.py** (26 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_invite_manager.py** (22 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **auth/dependencies.py** (19 connections) — `server/auth/dependencies.py`
- **invites.py** (19 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **asyncio** (14 connections)
- **models/invite.py** (13 connections) — `server/models/invite.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **asyncio** (12 connections)
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **.validate_invite()** (6 connections) — `server/auth/invites.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **test_get_current_superuser_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **test_get_current_superuser_success()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- *... and 100 more nodes in this community*

## Relationships

- [claude rules fastapi](claude_rules_fastapi.md) (25 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (19 shared connections)
- [characterinfo](characterinfo.md) (14 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (10 shared connections)
- [get current active user](get_current_active_user.md) (6 shared connections)
- [server game skill service](server_game_skill_service.md) (5 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (3 shared connections)
- [authenticationbackend](authenticationbackend.md) (2 shared connections)
- [server models game rationale 108](server_models_game_rationale_108.md) (1 shared connections)
- [server api admin subject controller](server_api_admin_subject_controller.md) (1 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 263 (81%)
- INFERRED: 61 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*