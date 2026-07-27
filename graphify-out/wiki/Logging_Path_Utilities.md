# Logging Path Utilities

> 78 nodes · cohesion 0.05

## Key Concepts

- **test_logging_utilities.py** (39 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **Path** (23 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **rotate_log_files()** (18 connections) — `server/structured_logging/logging_utilities.py`
- **detect_environment()** (16 connections) — `server/structured_logging/logging_utilities.py`
- **resolve_log_base()** (13 connections) — `server/structured_logging/logging_utilities.py`
- **Path** (4 connections) — `server/structured_logging/logging_utilities.py`
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
- **test_rotate_log_files_handles_permission_error()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_no_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_non_windows_platform()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_recursive_search()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- *... and 53 more nodes in this community*

## Relationships

- [[Logging File Setup]] (9 shared connections)
- [[NPC Admin API]] (7 shared connections)
- [[Logging Structured Player]] (6 shared connections)
- [[Logging Rotating Handlers]] (3 shared connections)
- [[Logging Structured Handlers]] (2 shared connections)

## Source Files

- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_utilities.py`

## Audit Trail

- EXTRACTED: 298 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
