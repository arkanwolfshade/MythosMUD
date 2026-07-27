# Motd Loader

> 12 nodes · cohesion 0.23

## Key Concepts

- **load_motd()** (8 connections) — `server/utils/motd_loader.py`
- **test_motd_loader.py** (6 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **test_load_motd_empty_file()** (3 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **test_load_motd_file_exists()** (3 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **test_load_motd_file_not_exists()** (3 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **test_load_motd_file_read_error()** (3 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **Load the Message of the Day from the configured file.      Returns:         str:** (1 connections) — `server/utils/motd_loader.py`
- **Unit tests for motd_loader utilities.  Tests the MOTD loading functions.** (1 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **Test load_motd() loads MOTD from file.** (1 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **Test load_motd() returns default when file doesn't exist.** (1 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **Test load_motd() handles file read errors.** (1 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **Test load_motd() handles empty file.** (1 connections) — `server/tests/unit/utils/test_motd_loader.py`

## Relationships

- [[NPC Admin API]] (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_motd_loader.py`
- `server/utils/motd_loader.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
