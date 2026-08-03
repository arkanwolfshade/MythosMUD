# player requests schemas

> 75 nodes

## Key Concepts

- **Invite** (38 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **.validate_invite()** (6 connections) — `server/auth/invites.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **.create_invite()** (4 connections) — `server/auth/invites.py`
- **.get_user_invites()** (4 connections) — `server/auth/invites.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **UUID** (3 connections)
- **.get_unused_invites()** (3 connections) — `server/auth/invites.py`
- **.cleanup_expired_invites()** (3 connections) — `server/auth/invites.py`
- **.is_expired()** (3 connections) — `server/models/invite.py`
- **.is_valid()** (3 connections) — `server/models/invite.py`
- **test_invite_is_expired_with_future_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_past_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_aware_datetime()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_active_and_not_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive()** (3 connections) — `server/tests/unit/models/test_invite.py`
- *... and 50 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (16 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (5 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [command commands talk](command_commands_talk.md) (1 shared connections)
- [models invite Any](models_invite_Any.md) (1 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)
- [logging file setup](logging_file_setup.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 231 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*