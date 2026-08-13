# log_and_raise

> 53 nodes

## Key Concepts

- **log_and_raise()** (174 connections) — `server/utils/error_logging.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_decayed_containers()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (11 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (11 connections) — `server/persistence/container_query_helpers.py`
- **.update_player_xp()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.get_all_spells()** (6 connections) — `server/persistence/repositories/spell_repository.py`
- **.get_spell_by_id()** (6 connections) — `server/persistence/repositories/spell_repository.py`
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.get_skill_ids_used_at_level()** (5 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **.record_use()** (5 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **_row_to_spell_dict()** (5 connections) — `server/persistence/repositories/spell_repository.py`
- **.list_quest_ids_offered_by()** (4 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **Any** (4 connections)
- **ContainerData** (4 connections)
- **.apply_corruption()** (3 connections) — `server/game/mechanics.py`
- **.apply_fear()** (3 connections) — `server/game/mechanics.py`
- **.apply_lucidity_loss()** (3 connections) — `server/game/mechanics.py`
- **.damage_player()** (3 connections) — `server/game/mechanics.py`
- **.gain_experience()** (3 connections) — `server/game/mechanics.py`
- **.heal_player()** (3 connections) — `server/game/mechanics.py`
- **.get_room_players()** (3 connections) — `server/game/movement_service.py`
- **UUID** (3 connections)
- *... and 28 more nodes in this community*

## Relationships

- [get_session_maker](get_session_maker.md) (29 shared connections)
- [DatabaseError](DatabaseError.md) (28 shared connections)
- [container_persistence_async.py](container_persistence_async.py.md) (20 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (17 shared connections)
- [.transfer_from_container](transfer_from_container.md) (13 shared connections)
- [MovementService](MovementService.md) (9 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (9 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (8 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (8 shared connections)
- [test_container_persistence.py](test_container_persistence.py.md) (7 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (6 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/persistence/container_query_helpers.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 283 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*