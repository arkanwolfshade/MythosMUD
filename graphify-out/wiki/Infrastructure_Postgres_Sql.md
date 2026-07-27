# Infrastructure Postgres Sql

> 20 nodes · cohesion 0.10

## Key Concepts

- **TestVerificationSqlUsersPlayers** (6 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **TestNpcNameConstraintScript** (5 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **test_postgres_sql_scripts.py** (3 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **.test_npc_constraint_script_exists()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **.test_npc_constraint_script_no_sqlite_pragma()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **.test_npc_constraint_script_uses_postgresql_constraint()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **.test_verification_sql_file_exists()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **.test_verification_sql_references_users_and_players()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **.test_verification_sql_uses_explicit_joins()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **.test_verification_sql_uses_live_tables_only()** (2 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **PostgreSQL-focused tests for verification and maintenance SQL scripts.  Validate** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **Tests for db/verification/users_players.sql alignment with current schema.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **Verification SQL file must exist.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **Verification SQL must not reference staging tables or select obsolete columns.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **Verification SQL must use explicit join syntax for multi-table queries.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **Verification SQL must reference users and players tables.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **Tests for server/scripts/add_npc_name_constraint.sql (PostgreSQL-only).** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **NPC name constraint script must exist.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **Script must not contain SQLite-specific pragma.** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`
- **Script must use PostgreSQL constraint (CHECK or ALTER TABLE).** (1 connections) — `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/tests/unit/infrastructure/test_postgres_sql_scripts.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
