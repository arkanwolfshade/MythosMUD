# Test Refactoring Complete

> 7 nodes

## Key Concepts

- **migration_schema_checks.py** (3 connections) — `server/scripts/migration_schema_checks.py`
- **table_exists()** (3 connections) — `server/scripts/migration_schema_checks.py`
- **column_exists()** (3 connections) — `server/scripts/migration_schema_checks.py`
- **AsyncConnection** (2 connections)
- **Shared schema existence checks for one-off migration scripts.** (1 connections) — `server/scripts/migration_schema_checks.py`
- **Return True if the named table exists in information_schema.** (1 connections) — `server/scripts/migration_schema_checks.py`
- **Return True if the named column exists on the table.** (1 connections) — `server/scripts/migration_schema_checks.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/scripts/migration_schema_checks.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*