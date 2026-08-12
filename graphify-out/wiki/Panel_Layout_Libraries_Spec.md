# Panel Layout Libraries Spec

> 5 nodes

## Key Concepts

- **.__call__()** (3 connections) — `server/utils/liability_types.py`
- **LiabilityStackEntry** (3 connections)
- **.__call__()** (3 connections) — `server/utils/liability_types.py`
- **Decode stored liability text (or empty state) into stack rows.** (1 connections) — `server/utils/liability_types.py`
- **Encode stack rows into JSON suitable for PlayerLucidity.liabilities.** (1 connections) — `server/utils/liability_types.py`

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (2 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (1 shared connections)

## Source Files

- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 10 (91%)
- INFERRED: 1 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*