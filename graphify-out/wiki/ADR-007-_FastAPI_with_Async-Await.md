# ADR-007: FastAPI with Async/Await

> 2 nodes

## Key Concepts

- **test_is_valid_target_name_valid()** (2 connections) — `server/tests/unit/validators/test_combat_validator.py`
- **Test _is_valid_target_name with valid target name.** (1 connections) — `server/tests/unit/validators/test_combat_validator.py`

## Relationships

- [test_optimized_security_validator.py](test_optimized_security_validator.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_combat_validator.py`

## Audit Trail

- EXTRACTED: 2 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*