# Player Domain Model

> 135 nodes · cohesion 0.02

## Key Concepts

- **Player** (185 connections) — `server/models/player.py`
- **test_player_model.py** (46 connections) — `server/tests/unit/models/test_player_model.py`
- **PlayerInventory** (30 connections) — `server/models/player.py`
- **PositionState** (19 connections) — `server/models/game.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **player_repository_mappers.py** (9 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **player_repository_save.py** (9 connections) — `server/persistence/repositories/player_repository_save.py`
- **Any** (7 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_coerce_row_stats()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_numerics()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_strings()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **InventoryPayload** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_parse_equipped_safely()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **datetime** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **_convert_legacy_stats_string()** (3 connections) — `server/models/player.py`
- **test_player_add_experience()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_add_experience_zero()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_apply_dp_change_became_dead()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_apply_dp_change_became_mortally_wounded()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_apply_dp_change_updates_dp()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_apply_dp_decay_caps_at_negative_10()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_apply_dp_decay_changes_posture_when_crossing_zero()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_apply_dp_decay_reduces_dp()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_creation()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- **test_player_defaults()** (3 connections) — `server/tests/unit/models/test_player_model.py`
- *... and 110 more nodes in this community*

## Relationships

- [[NPC Admin API]] (31 shared connections)
- [[SQLAlchemy Model Base]] (22 shared connections)
- [[Lucidity Database Models]] (14 shared connections)
- [[Player Save Preparer]] (13 shared connections)
- [[Integer Coercion Utils]] (11 shared connections)
- [[Admin Summon Command]] (9 shared connections)
- [[Integration DB Fixtures]] (7 shared connections)
- [[Room Occupancy Class]] (7 shared connections)
- [[Player Related Models]] (6 shared connections)
- [[Player Death Service]] (6 shared connections)
- [[Health Cold Resistance]] (5 shared connections)
- [[Persistence Repositories Player]] (3 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/player.py`
- `server/models/player_spells.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_save.py`
- `server/tests/unit/models/test_player_model.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 492 (85%)
- INFERRED: 84 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
