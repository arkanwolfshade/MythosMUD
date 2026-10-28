# P3 · container-di + client + domain

> 10 nodes · cohesion 0.20

## Key Concepts

- **security_utils.py** (8 connections) — `server/security_utils.py`
- **ensure_directory_exists()** (6 connections) — `server/security_utils.py`
- **test_ensure_directory_exists_creates()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_ensure_directory_exists_existing()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **test_ensure_directory_exists_relative_path()** (3 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Security utilities for MythosMUD server. Implements secure path validation and…** (1 connections) — `server/security_utils.py`
- **Ensure a directory exists and return its absolute path. Args: directory: The…** (1 connections) — `server/security_utils.py`
- **Test ensure_directory_exists with existing directory.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test ensure_directory_exists creates directory if it doesn't exist.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`
- **Test ensure_directory_exists with relative path.** (1 connections) — `server/tests/unit/infrastructure/test_security_utils.py`

## Relationships

- [ascii_map_exits.py](ascii_map_exits.py.md) (6 shared connections)
- [Room](Room.md) (2 shared connections)
- [Adapt Skill](Adapt_Skill.md) (1 shared connections)
- [directionHallucination.ts](directionHallucination.ts.md) (1 shared connections)

## Source Files

- `server/security_utils.py`
- `server/tests/unit/infrastructure/test_security_utils.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*