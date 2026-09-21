# player_spell_repository.py

> 42 nodes

## Key Concepts

- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **PlayerSpell** (19 connections) — `server/models/player_spells.py`
- **test_player_spell_repository.py** (19 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
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
- *... and 17 more nodes in this community*

## Relationships

- [lifespan_magic.py](lifespan_magic.py.md) (11 shared connections)
- [DatabaseError](DatabaseError.md) (10 shared connections)
- [server/models/__init__.py](server-models-__init__.py.md) (6 shared connections)
- [get_session_maker](get_session_maker.md) (6 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (1 shared connections)
- [magic_service.py](magic_service.py.md) (1 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (1 shared connections)
- [Spell](Spell.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)

## Source Files

- `server/models/player_spells.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/models/test_player_spells.py`
- `server/tests/unit/persistence/test_player_spell_repository.py`

## Audit Trail

- EXTRACTED: 115 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*