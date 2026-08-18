# server structured logging logging utilities

> 90 nodes

## Key Concepts

- **test_logging_utilities.py** (41 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **ensure_log_directory()** (24 connections) — `server/structured_logging/logging_utilities.py`
- **logging_utilities.py** (23 connections) — `server/structured_logging/logging_utilities.py`
- **Path** (23 connections)
- **rotate_log_files()** (19 connections) — `server/structured_logging/logging_utilities.py`
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
- **test_rotate_log_files_handles_jsonl_files()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- *... and 65 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (19 shared connections)
- [logger](logger.md) (9 shared connections)
- [server structured logging logging handlers](server_structured_logging_logging_handlers.md) (6 shared connections)
- [formatter](formatter.md) (4 shared connections)
- [server structured logging player guid](server_structured_logging_player_guid.md) (2 shared connections)
- [claude rules click](claude_rules_click.md) (2 shared connections)
- [eventdict](eventdict.md) (1 shared connections)
- [claude rules structlog](claude_rules_structlog.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_utilities.py`

## Audit Trail

- EXTRACTED: 188 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*