# Real-Time Architecture Docs

> 27 nodes

## Key Concepts

- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **test_project_paths.py** (10 connections) — `server/tests/unit/utils/test_project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **.__init__()** (8 connections) — `server/services/holiday_service.py`
- **.__init__()** (7 connections) — `server/services/schedule_service.py`
- **._load_from_database()** (4 connections) — `server/services/holiday_service.py`
- **test_get_project_root()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_normalize_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_environment_data_dir()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **test_get_calendar_paths_for_environment()** (3 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Path** (3 connections)
- **Path** (2 connections)
- **Path** (2 connections)
- **Load holidays from PostgreSQL database.** (1 connections) — `server/services/holiday_service.py`
- **Unit tests for project_paths utilities.  Tests path resolution functions.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Test get_project_root() returns project root path.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Test normalize_environment() normalizes environment names.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Test get_environment_data_dir() returns data directory.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Test get_calendar_paths_for_environment() returns calendar paths.** (1 connections) — `server/tests/unit/utils/test_project_paths.py`
- **Project path resolution helpers used across runtime code and tooling.** (1 connections) — `server/utils/project_paths.py`
- **Return the repository root (directory containing pyproject.toml).** (1 connections) — `server/utils/project_paths.py`
- **Normalize logging environment names to their canonical directory names.** (1 connections) — `server/utils/project_paths.py`
- *... and 2 more nodes in this community*

## Relationships

- [ASCII Map API](ASCII_Map_API.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (5 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (5 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (4 shared connections)
- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (2 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)

## Source Files

- `server/services/holiday_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 118 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*