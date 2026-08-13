# generate_invites_db.py

> 25 nodes

## Key Concepts

- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **reset_database()** (8 connections) — `server/database_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **reset_db()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_reset_database()** (4 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites_db.py`
- **datetime** (3 connections)
- **fixture** (1 connections)
- **Set test override database URL.** (1 connections) — `server/database_config_helpers.py`
- **Reset database state for testing. This function resets the DatabaseManager…** (1 connections) — `server/database_helpers.py`
- **Reset database state before each test.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Test reset_database resets DatabaseManager singleton and module state.** (1 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **Generate a unique Mythos-themed invite code.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate a list of unique invite codes.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Get existing invite codes from the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Create an invite in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Use DATABASE_URL so scripts can run without full AppConfig.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate invite codes and store them in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Parse YYYY-MM-DD to end-of-day UTC (naive). Invite valid through that date.** (1 connections) — `tools/invite_tools/generate_invites_db.py`

## Relationships

- [DatabaseError](DatabaseError.md) (6 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (5 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [reset_database](reset_database.md) (2 shared connections)
- [Invite](Invite.md) (2 shared connections)
- [.reset_instance](reset_instance.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [User](User.md) (1 shared connections)

## Source Files

- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*