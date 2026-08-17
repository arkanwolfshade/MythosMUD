# server tests unit persistence repositories

> 11 nodes

## Key Concepts

- **test_spell_repository.py** (15 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **asyncio** (4 connections)
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_spell_row()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **fixture** (1 connections)
- **Unit tests for SpellRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Relationships

- [server app lifespan magic](server_app_lifespan_magic.md) (2 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (2 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Audit Trail

- EXTRACTED: 25 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*