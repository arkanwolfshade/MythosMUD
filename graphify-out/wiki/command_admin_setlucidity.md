# command admin setlucidity

> 34 nodes

## Key Concepts

- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **experience_repository.py** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **.update_player_xp()** (7 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_occult_knowledge()** (6 connections) — `server/game/mechanics.py`
- **.gain_experience()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/mechanics.py`
- **UUID** (5 connections)
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **test_update_player_xp_player_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **Any** (2 connections)
- **Player** (2 connections)
- **repo()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_negative_amount()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_success()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_publishes_event()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_negative_delta()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_success()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_name()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_delta_type()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_success()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **Initialize the async persistence layer.          This facade delegates to focuse** (1 connections) — `server/async_persistence.py`
- *... and 9 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (22 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [world models rationale](world_models_rationale.md) (4 shared connections)
- [room persistence loader](room_persistence_loader.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [persistence container item](persistence_container_item.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [command commands service](command_commands_service.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/game/mechanics.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 137 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*