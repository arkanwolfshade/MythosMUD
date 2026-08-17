# server structured logging logging utilities

> 92 nodes

## Key Concepts

- **test_logging_utilities.py** (41 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **Path** (23 connections)
- **logging_utilities.py** (22 connections) — `server/structured_logging/logging_utilities.py`
- **rotate_log_files()** (19 connections) — `server/structured_logging/logging_utilities.py`
- **detect_environment()** (16 connections) — `server/structured_logging/logging_utilities.py`
- **resolve_log_base()** (13 connections) — `server/structured_logging/logging_utilities.py`
- **_rotate_single_log_file()** (6 connections) — `server/structured_logging/logging_utilities.py`
- **Path** (6 connections)
- **_rename_or_copy_log_file()** (5 connections) — `server/structured_logging/logging_utilities.py`
- **_collect_rotatable_logs()** (4 connections) — `server/structured_logging/logging_utilities.py`
- **_rotation_bound_logger()** (4 connections) — `server/structured_logging/logging_utilities.py`
- **test_ensure_log_directory_creates_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_empty_path()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_existing_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_no_parent()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_os_error()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_permission_error()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_thread_safety()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_absolute_path()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_env_local_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_finds_pyproject_in_parent()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_relative_path_no_pyproject()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_relative_path_with_pyproject()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_empty_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- *... and 67 more nodes in this community*

## Relationships

- [formatter](formatter.md) (15 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [claude rules structlog](claude_rules_structlog.md) (3 shared connections)
- [eventdict](eventdict.md) (2 shared connections)
- [server structured logging logging handlers](server_structured_logging_logging_handlers.md) (2 shared connections)
- [claude rules click](claude_rules_click.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_utilities.py`

## Audit Trail

- EXTRACTED: 190 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*