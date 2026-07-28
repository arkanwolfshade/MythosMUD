# Room File Fixer

> 31 nodes · cohesion 0.11

## Key Concepts

- **RoomFixer** (19 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Path** (7 connections)
- **.fix_schema_issues()** (7 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **.create_backup()** (6 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **.load_room_file()** (6 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **.save_room_file()** (6 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **._create_backup_if_requested()** (5 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **.fix_bidirectional_connections()** (5 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **._fix_missing_fields()** (5 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **.fix_self_references()** (5 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **._save_fixed_room()** (5 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **._find_room_file()** (4 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **._fix_missing_exits()** (3 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **._fix_missing_optional_fields()** (3 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **.__init__()** (3 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **.get_fix_summary()** (2 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Fix self-references by adding proper flags.          Args:             room_data** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Automatically fixes common room validation issues.      Implements safe correcti** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Find the file for a room. Returns None if file doesn't exist.** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Create backup if requested.** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Fix missing exits field. Returns True if fixed.** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Fix missing optional fields. Returns True if any fixed.** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Initialize the room fixer.          Args:             base_path: Base directory** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Fix missing fields based on errors. Returns True if any fixed.** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- **Save fixed room if changes were made.** (1 connections) — `tools/room_toolkit/room_validator/core/fixer.py`
- *... and 6 more nodes in this community*

## Relationships

- [Room Fixer Toolkit](Room_Fixer_Toolkit.md) (4 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/fixer.py`

## Audit Trail

- EXTRACTED: 106 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*