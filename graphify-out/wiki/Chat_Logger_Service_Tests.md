# Chat Logger Service Tests

> 18 nodes

## Key Concepts

- **ProfessionRepository** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **_row_to_profession()** (9 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_all_professions()** (7 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_profession_by_id()** (7 connections) — `server/persistence/repositories/profession_repository.py`
- **Any** (5 connections)
- **_text_or_default()** (4 connections) — `server/persistence/repositories/profession_repository.py`
- **_bool_or_default()** (4 connections) — `server/persistence/repositories/profession_repository.py`
- **Profession** (4 connections)
- **_str_or_default()** (3 connections) — `server/persistence/repositories/profession_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/profession_repository.py`
- **Return value as str or a default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return text value or default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return bool(value) when not None, otherwise default.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Map procedure result row to Profession model.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Repository for profession persistence operations.      Handles profession querie** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Initialize the profession repository.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Get all available professions.          Returns:             list[Profession]: L** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Get a profession by ID.          Args:             profession_id: Profession ID** (1 connections) — `server/persistence/repositories/profession_repository.py`

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (9 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (5 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (2 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/profession_repository.py`

## Audit Trail

- EXTRACTED: 59 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*