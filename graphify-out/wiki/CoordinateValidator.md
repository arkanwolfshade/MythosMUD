# CoordinateValidator

> 25 nodes

## Key Concepts

- **.claude/hooks/record_edited_file.py** (11 connections) — `.claude/hooks/record_edited_file.py`
- **_is_test_file()** (7 connections) — `.claude/hooks/record_edited_file.py`
- **main()** (7 connections) — `.claude/hooks/record_edited_file.py`
- **_should_skip_recording()** (5 connections) — `.claude/hooks/record_edited_file.py`
- **Path** (5 connections)
- **_is_client_test_path()** (4 connections) — `.claude/hooks/record_edited_file.py`
- **_load_payload()** (4 connections) — `.claude/hooks/record_edited_file.py`
- **_load_state()** (4 connections) — `.claude/hooks/record_edited_file.py`
- **_normalize_path()** (4 connections) — `.claude/hooks/record_edited_file.py`
- **_rel_path()** (4 connections) — `.claude/hooks/record_edited_file.py`
- **_write_state_atomic()** (4 connections) — `.claude/hooks/record_edited_file.py`
- **_is_agent_config_path()** (3 connections) — `.claude/hooks/record_edited_file.py`
- **_is_server_test_path()** (3 connections) — `.claude/hooks/record_edited_file.py`
- **Any** (2 connections)
- **Write state via a same-directory temp file + os.replace so a concurrent…** (1 connections) — `.claude/hooks/record_edited_file.py`
- **Return True if we should not record (missing data or test file).** (1 connections) — `.claude/hooks/record_edited_file.py`
- **Entry point: read hook payload from stdin and record non-test edited files to…** (1 connections) — `.claude/hooks/record_edited_file.py`
- **Normalize path to forward slashes for consistent matching.** (1 connections) — `.claude/hooks/record_edited_file.py`
- **Return workspace-relative path for pattern matching.** (1 connections) — `.claude/hooks/record_edited_file.py`
- **True if path is under server/tests/.** (1 connections) — `.claude/hooks/record_edited_file.py`
- **True if path is in __tests__/ or has client test extension.** (1 connections) — `.claude/hooks/record_edited_file.py`
- **True if path is under .claude/ or .cursor/ (agent/skill/rule/hook config, not…** (1 connections) — `.claude/hooks/record_edited_file.py`
- **Return True if the file should NOT trigger the test agent: a test file, or…** (1 connections) — `.claude/hooks/record_edited_file.py`
- **Load JSON payload from stdin; return None on failure (fail open).** (1 connections) — `.claude/hooks/record_edited_file.py`
- **Load state from file; return empty dict on failure.** (1 connections) — `.claude/hooks/record_edited_file.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `.claude/hooks/record_edited_file.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*