# PlayerSpellRepository

> 35 nodes

## Key Concepts

- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **test_player_spell_repository.py** (20 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **_row_to_player_spell()** (11 connections) — `server/persistence/repositories/player_spell_repository.py`
- **_mock_session_with_rows()** (9 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **asyncio** (9 connections)
- **.get_player_spell()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.get_player_spells()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.learn_spell()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.record_spell_cast()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.update_mastery()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **_spell_row()** (6 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **UUID** (6 connections)
- **test_get_player_spell_found()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spells()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_learn_spell()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_learn_spell_no_row_raises()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_record_spell_cast()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_update_mastery()** (4 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/player_spell_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spell_missing()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spells_db_error()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_update_mastery_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_row_to_player_spell_maps_fields()** (2 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **Any** (1 connections)
- *... and 10 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (14 shared connections)
- [Player](Player.md) (11 shared connections)
- [get_session_maker](get_session_maker.md) (5 shared connections)
- [log_and_raise](log_and_raise.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (3 shared connections)
- [SpellLearningService](SpellLearningService.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/persistence/test_player_spell_repository.py`

## Audit Trail

- EXTRACTED: 103 (88%)
- INFERRED: 14 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*