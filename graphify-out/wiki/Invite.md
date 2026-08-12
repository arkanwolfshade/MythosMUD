# Invite

> 72 nodes

## Key Concepts

- **Invite** (34 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **models/invite.py** (10 connections) — `server/models/invite.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **.get_unused_invites()** (3 connections) — `server/auth/invites.py`
- **.is_expired()** (3 connections) — `server/models/invite.py`
- **.is_valid()** (3 connections) — `server/models/invite.py`
- **test_invite_create_invite_defaults()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_creator()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_custom_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_format()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_uniqueness()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_aware_datetime()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_future_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- *... and 47 more nodes in this community*

## Relationships

- [User](User.md) (11 shared connections)
- [Player](Player.md) (7 shared connections)
- [database.py](database.py.md) (5 shared connections)
- [log_and_raise](log_and_raise.md) (5 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/database_config_helpers.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 230 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*