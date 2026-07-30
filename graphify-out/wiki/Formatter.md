# Formatter

> 25 nodes

## Key Concepts

- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **test_get_project_root()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_normalize_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_environment_data_dir()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_calendar_paths_for_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Path** (3 connections)
- **Path** (2 connections)
- **Path** (2 connections)
- **Unit tests for project_paths utilities.  Tests path resolution functions.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Test get_project_root() returns project root path.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Test normalize_environment() normalizes environment names.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Test get_environment_data_dir() returns data directory.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Test get_calendar_paths_for_environment() returns calendar paths.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Project path resolution helpers used across runtime code and tooling.** (1 connections) — `server/utils/project_paths.py`
- **Return the repository root (directory containing pyproject.toml).** (1 connections) — `server/utils/project_paths.py`
- **Normalize logging environment names to their canonical directory names.** (1 connections) — `server/utils/project_paths.py`
- **Compute the base data directory for the provided environment.** (1 connections) — `server/utils/project_paths.py`
- **Return (holidays_file, schedules_dir) for the requested environment.** (1 connections) — `server/utils/project_paths.py`

## Relationships

- [hash password()](hash_password%28%29.md) (8 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (7 shared connections)
- [HolidayCollection](HolidayCollection.md) (7 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (7 shared connections)
- [test command parser](test_command_parser.md) (6 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (2 shared connections)

## Source Files

- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 113 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*