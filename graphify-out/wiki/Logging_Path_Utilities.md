# Logging Path Utilities

> 92 nodes

## Key Concepts

- **test_logging_utilities.py** (40 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **ensure_log_directory()** (23 connections) — `server/structured_logging/logging_utilities.py`
- **Path** (23 connections)
- **logging_utilities.py** (19 connections) — `server/structured_logging/logging_utilities.py`
- **rotate_log_files()** (19 connections) — `server/structured_logging/logging_utilities.py`
- **detect_environment()** (16 connections) — `server/structured_logging/logging_utilities.py`
- **resolve_log_base()** (13 connections) — `server/structured_logging/logging_utilities.py`
- **temp_dir()** (11 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **_prepare_log_environment()** (9 connections) — `server/structured_logging/logging_file_setup.py`
- **Path** (5 connections)
- **_rotate_single_log_file()** (5 connections) — `server/structured_logging/logging_utilities.py`
- **_rotation_bound_logger()** (4 connections) — `server/structured_logging/logging_utilities.py`
- **_collect_rotatable_logs()** (4 connections) — `server/structured_logging/logging_utilities.py`
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
- *... and 67 more nodes in this community*

## Relationships

- [Logging File Setup](Logging_File_Setup.md) (13 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Logging Structured Handlers](Logging_Structured_Handlers.md) (6 shared connections)
- [Admin Set Stat Command](Admin_Set_Stat_Command.md) (4 shared connections)
- [Room Definition Loader](Room_Definition_Loader.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Logging Structured Player](Logging_Structured_Player.md) (2 shared connections)
- [Logging Structured Processors](Logging_Structured_Processors.md) (2 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (1 shared connections)
- [Security Sanitization Planning](Security_Sanitization_Planning.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/structured_logging/logging_utilities.py`
- `server/tests/unit/structured_logging/test_logging_utilities.py`

## Audit Trail

- EXTRACTED: 350 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*