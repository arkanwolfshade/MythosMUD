# security headers middleware

> 4 nodes

## Key Concepts

- **.to_dict()** (4 connections) — `server/exceptions.py`
- **._log_error()** (2 connections) — `server/exceptions.py`
- **Log the error with structured context.** (2 connections) — `server/exceptions.py`
- **Convert error to dictionary for API responses.** (1 connections) — `server/exceptions.py`

## Relationships

- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [Spell Validation](Spell_Validation.md) (1 shared connections)

## Source Files

- `server/exceptions.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*