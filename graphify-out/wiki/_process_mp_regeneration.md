# _process_mp_regeneration

> 8 nodes

## Key Concepts

- **_process_mp_regeneration()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_processing.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_processing.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_mp_regeneration_services()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Validate that required services exist for MP regeneration. Args: container:…** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for a single player. Args: mp_service: MP regeneration…** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for online players.** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (6 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (6 shared connections)
- [_process_mortally_wounded_player](_process_mortally_wounded_player.md) (2 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*