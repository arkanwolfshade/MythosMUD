# Architecture Container System

> 6 nodes

## Key Concepts

- **sqlint.py** (4 connections) — `scripts/sqlint.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **_skip_sqlint()** (1 connections) — `scripts/sqlint.py`
- **Return True when sqlint failed to start rather than reporting SQL issues.** (1 connections) — `scripts/sqlint.py`
- **Return sqlint command argv when the tool is installed and runnable.** (1 connections) — `scripts/sqlint.py`

## Relationships

- [CI Quality Scripts](CI_Quality_Scripts.md) (1 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (1 shared connections)

## Source Files

- `scripts/sqlint.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*