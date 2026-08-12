# Container Repository CRUD

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

- [Chat Channel Logger](Chat_Channel_Logger.md) (8 shared connections)
- [Error Handling Guide](Error_Handling_Guide.md) (7 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (6 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (4 shared connections)
- [Combat Messaging Base](Combat_Messaging_Base.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Spell Effects Tests](Spell_Effects_Tests.md) (2 shared connections)
- [Minimap Fallback Helpers](Minimap_Fallback_Helpers.md) (1 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)

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