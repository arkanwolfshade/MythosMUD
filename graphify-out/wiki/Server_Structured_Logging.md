# Server Structured Logging

> 84 nodes

## Key Concepts

- **test_logging_utilities.py** (40 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **Path** (23 connections)
- **rotate_log_files()** (18 connections) — `server/structured_logging/logging_utilities.py`
- **logging_utilities.py** (17 connections) — `server/structured_logging/logging_utilities.py`
- **resolve_log_base()** (13 connections) — `server/structured_logging/logging_utilities.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **_rotation_bound_logger()** (4 connections) — `server/structured_logging/logging_utilities.py`
- **test_ensure_log_directory_creates_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_existing_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_no_parent()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_empty_path()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_permission_error()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_os_error()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_ensure_log_directory_thread_safety()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_absolute_path()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_relative_path_with_pyproject()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_relative_path_no_pyproject()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_finds_pyproject_in_parent()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_resolve_log_base_env_local_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_no_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_empty_directory()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_rotates_log_files()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_skips_empty_files()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **test_rotate_log_files_handles_permission_error()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- *... and 59 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (18 shared connections)
- [Server Structured Logging (5)](Server_Structured_Logging_%285%29.md) (13 shared connections)
- [Server Structured Logging (6)](Server_Structured_Logging_%286%29.md) (4 shared connections)
- [Server Structured Logging (3)](Server_Structured_Logging_%283%29.md) (2 shared connections)
- [Server Structured Logging (15)](Server_Structured_Logging_%2815%29.md) (2 shared connections)
- [Tools Room Toolkit](Tools_Room_Toolkit.md) (2 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_utilities.py`

## Audit Trail

- EXTRACTED: 314 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*