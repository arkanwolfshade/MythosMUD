# server tests unit persistence test

> 17 nodes

## Key Concepts

- **test_player_spell_repository.py** (20 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **_mock_session_with_rows()** (9 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **asyncio** (9 connections)
- **_spell_row()** (6 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spell_found()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spells()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_learn_spell()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_learn_spell_no_row_raises()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_record_spell_cast()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_update_mastery()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spell_missing()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spells_db_error()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_update_mastery_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_row_to_player_spell_maps_fields()** (2 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **fixture** (1 connections)
- **Unit tests for PlayerSpellRepository.** (1 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`

## Relationships

- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (3 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (2 shared connections)
- [server game skill service](server_game_skill_service.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_player_spell_repository.py`

## Audit Trail

- EXTRACTED: 44 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*