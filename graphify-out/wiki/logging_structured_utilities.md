# logging structured utilities

> 80 nodes

## Key Concepts

- **test_logging_utilities.py** (40 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **Path** (23 connections)
- **rotate_log_files()** (18 connections) — `server/structured_logging/logging_utilities.py`
- **resolve_log_base()** (13 connections) — `server/structured_logging/logging_utilities.py`
- **temp_dir()** (11 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
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
- **test_rotate_log_files_windows_platform()** (4 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- *... and 55 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (15 shared connections)
- [logging setup structured](logging_setup_structured.md) (10 shared connections)
- [manager subject services](manager_subject_services.md) (6 shared connections)
- [logging handlers structured](logging_handlers_structured.md) (5 shared connections)
- [validator room toolkit](validator_room_toolkit.md) (4 shared connections)
- [room toolkit validator](room_toolkit_validator.md) (3 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_utilities.py`

## Audit Trail

- EXTRACTED: 292 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*