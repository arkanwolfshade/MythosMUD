# Test Spell Repository

> 21 nodes

## Key Concepts

- **spell_repository.py** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **test_spell_repository.py** (15 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_row_to_spell_dict()** (7 connections) — `server/persistence/repositories/spell_repository.py`
- **.get_all_spells()** (6 connections) — `server/persistence/repositories/spell_repository.py`
- **.get_spell_by_id()** (6 connections) — `server/persistence/repositories/spell_repository.py`
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **asyncio** (4 connections)
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_spell_row()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **Any** (3 connections)
- **test_row_to_spell_dict_maps_fields()** (2 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **fixture** (1 connections)
- **Spell repository for async persistence operations. This module provides async…** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **Get a spell by ID. Args: spell_id: Spell ID Returns: dict | None: Spell…** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **Map procedure result row to spell dict.** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **Get all spells from the database. Returns: list[dict]: List of all spell…** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **Unit tests for SpellRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Relationships

- [Wearable Container Service](Wearable_Container_Service.md) (6 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (6 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (5 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Spell](Test_Spell.md) (1 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)
- [Database](Database.md) (1 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Audit Trail

- EXTRACTED: 54 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*