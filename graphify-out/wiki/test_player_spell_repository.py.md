# test_player_spell_repository.py

> 40 nodes

## Key Concepts

- **test_player_spell_repository.py** (20 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **PlayerSpell** (19 connections) — `server/models/player_spells.py`
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
- **test_player_spells.py** (4 connections) — `server/tests/unit/models/test_player_spells.py`
- **test_player_spell_repr()** (3 connections) — `server/tests/unit/models/test_player_spells.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spell_missing()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_get_player_spells_db_error()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **test_update_mastery_not_found()** (3 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **.__repr__()** (2 connections) — `server/models/player_spells.py`
- *... and 15 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (12 shared connections)
- [get_session_maker](get_session_maker.md) (10 shared connections)
- [log_and_raise](log_and_raise.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)

## Source Files

- `server/models/player_spells.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/models/test_player_spells.py`
- `server/tests/unit/persistence/test_player_spell_repository.py`

## Audit Trail

- EXTRACTED: 97 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*