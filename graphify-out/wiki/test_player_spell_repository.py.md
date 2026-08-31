# test_player_spell_repository.py

> 31 nodes

## Key Concepts

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
- **repo()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spell_missing()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spells_db_error()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_update_mastery_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_row_to_player_spell_maps_fields()** (2 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **Any** (1 connections)
- **fixture** (1 connections)
- **Learn a new spell for a player. Args: player_id: Player ID spell_id: Spell ID…** (1 connections) — `server/persistence/repositories/player_spell_repository.py`
- *... and 6 more nodes in this community*

## Relationships

- [sqlalchemy.md](sqlalchemy.md.md) (9 shared connections)
- [SpellEffects](SpellEffects.md) (7 shared connections)
- [get_session_maker](get_session_maker.md) (5 shared connections)
- [log_and_raise](log_and_raise.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/persistence/test_player_spell_repository.py`

## Audit Trail

- EXTRACTED: 84 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*