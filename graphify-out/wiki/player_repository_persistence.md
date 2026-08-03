# player repository persistence

> 4 nodes

## Key Concepts

- **test_validate_secure_path_with_backslash()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_validate_secure_path_path_traversal_commonpath()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path normalizes backslashes.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test validate_secure_path detects path traversal via commonpath check.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`

## Relationships

- [security infrastructure path](security_infrastructure_path.md) (2 shared connections)
- [security infrastructure secure](security_infrastructure_secure.md) (2 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_security_utils.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*