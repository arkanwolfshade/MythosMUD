# CastingStateManager

> 34 nodes

## Key Concepts

- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **UUID** (8 connections)
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
- **.complete_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.get_casting_state()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.interrupt_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **test_update_casting_progress_waits_for_initiative()** (4 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **.get_all_casting_players()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **.is_casting()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **.update_casting_progress()** (3 connections) — `server/game/magic/casting_state_manager.py`
- **test_get_all_casting_players_and_clear()** (3 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **test_interrupt_casting()** (3 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **test_start_and_complete_casting()** (3 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **test_start_casting_twice_raises()** (3 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **test_update_casting_progress_completes()** (3 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **.clear_all()** (2 connections) — `server/game/magic/casting_state_manager.py`
- **.__init__()** (2 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (1 connections)
- **SimpleNamespace** (1 connections)
- **Check if a player is currently casting. Args: player_id: Player ID to check…** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Get the casting state for a player. Args: player_id: Player ID Returns:…** (1 connections) — `server/game/magic/casting_state_manager.py`
- **Complete and remove a casting state. Args: player_id: Player ID Returns:…** (1 connections) — `server/game/magic/casting_state_manager.py`
- *... and 9 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (5 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (3 shared connections)
- [SpellEffects](SpellEffects.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`

## Audit Trail

- EXTRACTED: 68 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*