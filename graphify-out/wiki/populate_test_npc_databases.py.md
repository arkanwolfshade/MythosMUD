# populate_test_npc_databases.py

> 16 nodes

## Key Concepts

- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites_db.py`
- **datetime** (3 connections)
- **Generate a unique Mythos-themed invite code.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate a list of unique invite codes.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Get existing invite codes from the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Create an invite in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Use DATABASE_URL so scripts can run without full AppConfig.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate invite codes and store them in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Parse YYYY-MM-DD to end-of-day UTC (naive). Invite valid through that date.** (1 connections) — `tools/invite_tools/generate_invites_db.py`

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [Test Suite Refactoring Plan](Test_Suite_Refactoring_Plan.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*