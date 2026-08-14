# normalize_environment

> 23 nodes

## Key Concepts

- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **test_get_calendar_paths_for_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_environment_data_dir()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_project_root()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_normalize_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Path** (3 connections)
- **Path** (1 connections)
- **Unit tests for project_paths utilities. Tests path resolution functions.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
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

- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [HolidayCollection](HolidayCollection.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [HolidayService](HolidayService.md) (2 shared connections)
- [TestScheduleService](TestScheduleService.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/services/schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*