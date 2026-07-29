# generate invites db

> 16 nodes

## Key Concepts

- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **datetime** (3 connections)
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites_db.py`
- **Parse YYYY-MM-DD to end-of-day UTC (naive). Invite valid through that date.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate a unique Mythos-themed invite code.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate a list of unique invite codes.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Get existing invite codes from the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Create an invite in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Use DATABASE_URL so scripts can run without full AppConfig.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate invite codes and store them in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`

## Relationships

- [main()](main%28%29.md) (8 shared connections)
- [.use invite()](use_invite%28%29.md) (2 shared connections)
- [Base](Base.md) (1 shared connections)

## Source Files

- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*