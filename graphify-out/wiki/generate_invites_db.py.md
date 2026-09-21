# generate_invites_db.py

> 22 nodes

## Key Concepts

- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites_db.py`
- **datetime** (3 connections)
- **Set test override database URL.** (1 connections) — `server/database_config_helpers.py`
- **Normalize database URL for asyncpg. Args: database_url: Original database URL…** (1 connections) — `server/database_config_helpers.py`
- **Sync module-level and config test database URL overrides.** (1 connections) — `server/database.py`
- **Generate a unique Mythos-themed invite code.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate a list of unique invite codes.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Get existing invite codes from the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Create an invite in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Use DATABASE_URL so scripts can run without full AppConfig.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate invite codes and store them in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Parse YYYY-MM-DD to end-of-day UTC (naive). Invite valid through that date.** (1 connections) — `tools/invite_tools/generate_invites_db.py`

## Relationships

- [DatabaseError](DatabaseError.md) (9 shared connections)
- [DatabaseManager](DatabaseManager.md) (3 shared connections)
- [Invite](Invite.md) (3 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*