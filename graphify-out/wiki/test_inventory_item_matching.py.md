# test_inventory_item_matching.py

> 55 nodes · cohesion 0.06

## Key Concepts

- **profession_repository.py** (18 connections) — `server/persistence/repositories/profession_repository.py`
- **test_profession_repository.py** (18 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **RoomRepository** (16 connections) — `server/persistence/repositories/room_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **ProfessionRepository** (13 connections) — `server/persistence/repositories/profession_repository.py`
- **_row_to_profession()** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **room_repository.py** (8 connections) — `server/persistence/repositories/room_repository.py`
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **_bool_or_default()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_all_professions()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_profession_by_id()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **_text_or_default()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **_str_or_default()** (5 connections) — `server/persistence/repositories/profession_repository.py`
- **Any** (4 connections)
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **asyncio** (4 connections)
- **test_get_all_professions()** (4 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_profession_by_id()** (4 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_helpers_defaults()** (4 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/profession_repository.py`
- **Profession** (3 connections)
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **_profession_row()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_all_professions_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- *... and 30 more nodes in this community*

## Relationships

- [endpoints.py](endpoints.py.md) (11 shared connections)
- [Room](Room.md) (9 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (5 shared connections)
- [properties](properties.md) (4 shared connections)
- [.profession_to_dict](profession_to_dict.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (1 shared connections)
- [command_result_text](command_result_text.md) (1 shared connections)
- [command_guards.py](command_guards.py.md) (1 shared connections)
- [Async Remediation Final Report](Async_Remediation_Final_Report.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/repositories/test_profession_repository.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 126 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*