# NATS Subject Manager

> 24 nodes

## Key Concepts

- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **set_test_database_url()** (11 connections) — `server/database_config_helpers.py`
- **get_test_database_url()** (7 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **_sync_test_url_state()** (5 connections) — `server/database.py`
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **datetime** (3 connections)
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites_db.py`
- **Get test override database URL.** (2 connections) — `server/database_config_helpers.py`
- **Sync module-level and config test database URL overrides.** (1 connections) — `server/database.py`
- **Set test override database URL.** (1 connections) — `server/database_config_helpers.py`
- **Normalize database URL for asyncpg.      Args:         database_url: Original da** (1 connections) — `server/database_config_helpers.py`
- **Parse YYYY-MM-DD to end-of-day UTC (naive). Invite valid through that date.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate a unique Mythos-themed invite code.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate a list of unique invite codes.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Get existing invite codes from the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Create an invite in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Use DATABASE_URL so scripts can run without full AppConfig.** (1 connections) — `tools/invite_tools/generate_invites_db.py`
- **Generate invite codes and store them in the database.** (1 connections) — `tools/invite_tools/generate_invites_db.py`

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (4 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Combat Services Messaging](Combat_Services_Messaging.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 91 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*