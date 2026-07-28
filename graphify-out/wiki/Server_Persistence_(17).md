# Server Persistence (17)

> 14 nodes

## Key Concepts

- **_row_to_profession()** (9 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_all_professions()** (7 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_profession_by_id()** (7 connections) — `server/persistence/repositories/profession_repository.py`
- **Any** (5 connections)
- **_text_or_default()** (4 connections) — `server/persistence/repositories/profession_repository.py`
- **_bool_or_default()** (4 connections) — `server/persistence/repositories/profession_repository.py`
- **Profession** (4 connections)
- **_str_or_default()** (3 connections) — `server/persistence/repositories/profession_repository.py`
- **Return value as str or a default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return text value or default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return bool(value) when not None, otherwise default.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Map procedure result row to Profession model.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Get all available professions.          Returns:             list[Profession]: L** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Get a profession by ID.          Args:             profession_id: Profession ID** (1 connections) — `server/persistence/repositories/profession_repository.py`

## Relationships

- [Server Admin](Server_Admin.md) (6 shared connections)
- [Server Persistence](Server_Persistence.md) (4 shared connections)
- [Server Persistence (3)](Server_Persistence_%283%29.md) (2 shared connections)
- [Server Api](Server_Api.md) (2 shared connections)
- [Server Models (28)](Server_Models_%2828%29.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/profession_repository.py`

## Audit Trail

- EXTRACTED: 45 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*