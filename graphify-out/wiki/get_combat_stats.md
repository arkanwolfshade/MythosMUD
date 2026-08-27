# .get_combat_stats

> 13 nodes

## Key Concepts

- **GameConfig** (18 connections) — `server/config/models/game.py`
- **.validate_aliases_dir()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (3 connections) — `server/config/models/game.py`
- **test_game_config_tick_rate_accepts_positive_override()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_rejects_negative()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_rejects_zero()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **BaseSettings** (1 connections)
- **Game-specific configuration.** (1 connections) — `server/config/models/game.py`
- **Validate combat error threshold.** (1 connections) — `server/config/models/game.py`
- **Validate aliases directory path.** (1 connections) — `server/config/models/game.py`
- **Test GameConfig server_tick_rate accepts a valid positive override.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test GameConfig server_tick_rate rejects zero (#622: busy-spins the tick loop…** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test GameConfig server_tick_rate rejects negative values (#622: crashes the…** (1 connections) — `server/tests/unit/config/test_config_models.py`

## Relationships

- [is_postgres_url](is_postgres_url.md) (8 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [click Best Practices](click_Best_Practices.md) (3 shared connections)
- [test_build_room_objects_with_non_dict_attributes](test_build_room_objects_with_non_dict_attributes.md) (1 shared connections)

## Source Files

- `server/config/models/game.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 23 (82%)
- INFERRED: 5 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*