---
description: "PostgreSQL database naming and safety rules for MythosMUD: which databases (mythos_unit, mythos_e2e, mythos_dev) may be reset, and where production vs. test data lives."
paths:
  - "db/**"
  - "**/*.sql"
  - "server/tests/fixtures/integration/**"
  - "scripts/*postgres*"
  - "scripts/apply_procedures.ps1"
---

# PostgreSQL database names (MythosMUD)

## CRITICAL: Which databases may be reset

- **mythos_unit** and **mythos_e2e**: Safe to reset at will. Integration and E2E tests may truncate/delete.
- **mythos_dev**: **PROTECTED.** Do NOT delete or truncate anything in mythos_dev unless the user gives a
  **direct, explicit instruction** to do so. Tests and automation must never touch mythos_dev for cleanup.

## Enforcement

- Integration test fixtures (`server/tests/fixtures/integration/`) only allow `DATABASE_URL` when the database
  name is `mythos_unit` or `mythos_e2e`. If the URL points to `mythos_dev`, the fixtures raise and refuse to run.
- Do not add mythos_dev to any "allowed for truncation" or "test database" list.
- When writing scripts, migrations, or test utilities that could delete data, never target mythos_dev unless the
  user explicitly requested it.

## Database placement (production vs test)

- Production data: `/data/players/` and `/data/npcs/`
- Test data: `server/tests/data/players/` and `server/tests/data/npcs/`
- PostgreSQL only; `player_id` is UUID.
- All PostgreSQL CRUD must go through stored procedures/functions in `db/procedures/`, not new inline DML/DQL.

---

*Ported from `.cursor/rules/database-postgres-names.mdc` (always-on in Cursor). Path-scoped here rather than
always-loaded — if you're writing DB-adjacent code that this glob doesn't catch, ask about mythos_dev safety
explicitly rather than relying on this rule having loaded.*
