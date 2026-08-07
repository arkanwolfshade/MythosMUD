# room game service

> 31 nodes

## Key Concepts

- **profession_repository.py** (18 connections) — `server/persistence/repositories/profession_repository.py`
- **test_profession_repository.py** (18 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **ProfessionRepository** (13 connections) — `server/persistence/repositories/profession_repository.py`
- **_row_to_profession()** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_all_professions()** (7 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_profession_by_id()** (7 connections) — `server/persistence/repositories/profession_repository.py`
- **_text_or_default()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **_bool_or_default()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **_str_or_default()** (5 connections) — `server/persistence/repositories/profession_repository.py`
- **Any** (5 connections)
- **Profession** (4 connections)
- **test_helpers_defaults()** (4 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/profession_repository.py`
- **_profession_row()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_all_professions()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_profession_by_id()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_row_to_profession()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **repo()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_all_professions_db_error()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **Profession repository for async persistence operations.  This module provides as** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return value as str or a default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return text value or default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return bool(value) when not None, otherwise default.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- *... and 6 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (8 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (5 shared connections)
- [add used user](add_used_user.md) (4 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [room websocket updates](room_websocket_updates.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (1 shared connections)
- [commands party examples](commands_party_examples.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/profession_repository.py`
- `server/tests/unit/persistence/repositories/test_profession_repository.py`

## Audit Trail

- EXTRACTED: 131 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*