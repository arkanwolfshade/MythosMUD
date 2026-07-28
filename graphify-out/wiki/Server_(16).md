# Server (16)

> 5 nodes

## Key Concepts

- **test_run_cmd_decodes_subprocess_output_as_utf8()** (4 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **test_git_show_file_decodes_subprocess_output_as_utf8()** (4 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **MonkeyPatch** (2 connections)
- **Windows defaults text=True to cp1252; lizard/git can emit UTF-8 bytes (e.g. 0x8f** (1 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`
- **git show of UTF-8 sources must not use the Windows cp1252 locale codec.** (1 connections) — `server/tests/unit/test_quality_fragmentation_guard.py`

## Relationships

- [Server (7)](Server_%287%29.md) (2 shared connections)
- [Scripts Ci (3)](Scripts_Ci_%283%29.md) (1 shared connections)
- [Scripts Ci (2)](Scripts_Ci_%282%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_quality_fragmentation_guard.py`

## Audit Trail

- EXTRACTED: 10 (83%)
- INFERRED: 2 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*