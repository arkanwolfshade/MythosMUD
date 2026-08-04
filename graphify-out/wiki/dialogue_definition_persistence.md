# dialogue definition persistence

> 29 nodes

## Key Concepts

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
- **Return value as str or a default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return text value or default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return bool(value) when not None, otherwise default.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Map procedure result row to Profession model.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Repository for profession persistence operations.      Handles profession querie** (1 connections) — `server/persistence/repositories/profession_repository.py`
- *... and 4 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (15 shared connections)
- [profession models rationale](profession_models_rationale.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [persistence container item](persistence_container_item.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/profession_repository.py`
- `server/tests/unit/persistence/repositories/test_profession_repository.py`

## Audit Trail

- EXTRACTED: 112 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*