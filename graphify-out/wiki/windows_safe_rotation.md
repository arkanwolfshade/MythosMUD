# windows safe rotation

> 55 nodes

## Key Concepts

- **test_windows_safe_rotation.py** (23 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **WindowsSafeRotatingFileHandler** (20 connections) — `server/structured_logging/windows_safe_rotation.py`
- **Path** (12 connections)
- **WindowsSafeTimedRotatingFileHandler** (11 connections) — `server/structured_logging/windows_safe_rotation.py`
- **windows_safe_rotation.py** (7 connections) — `server/structured_logging/windows_safe_rotation.py`
- **test_windows_safe_rotating_file_handler_do_rollover_no_backup()** (4 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_rotating_file_handler_do_rollover_with_backup()** (4 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_rotating_file_handler_do_rollover_rotates_existing_backups()** (4 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_timed_rotating_file_handler_rotate_windows_platform()** (4 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_timed_rotating_file_handler_rotate_non_windows_platform()** (4 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_timed_rotating_file_handler_rotate_fallback_on_error()** (4 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **_copy_then_truncate()** (3 connections) — `server/structured_logging/windows_safe_rotation.py`
- **temp_log_file()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **temp_log_dir()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_copy_then_truncate_success()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_copy_then_truncate_creates_directory()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_copy_then_truncate_retries_on_failure()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_copy_then_truncate_raises_after_retries()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_rotating_file_handler_init()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_rotating_file_handler_do_rollover_handles_os_error()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_rotating_file_handler_do_rollover_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_rotating_file_handler_do_rollover_non_windows_platform()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_rotating_file_handler_do_rollover_no_stream()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_timed_rotating_file_handler_init()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- **test_windows_safe_timed_rotating_file_handler_rotation_filename()** (3 connections) — `server/tests/unit/structured_logging/test_windows_safe_rotation.py`
- *... and 30 more nodes in this community*

## Relationships

- [logging handlers structured](logging_handlers_structured.md) (4 shared connections)
- [logging setup structured](logging_setup_structured.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)

## Source Files

- `server/structured_logging/windows_safe_rotation.py`
- `server/tests/unit/structured_logging/test_windows_safe_rotation.py`

## Audit Trail

- EXTRACTED: 164 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*