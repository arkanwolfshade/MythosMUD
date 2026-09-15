# ExperienceRepository

> 51 nodes

## Key Concepts

- **ExperienceRepository** (26 connections) — `server/persistence/repositories/experience_repository.py`
- **RoomRepository** (16 connections) — `server/persistence/repositories/room_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **asyncio** (10 connections)
- **room_repository.py** (8 connections) — `server/persistence/repositories/room_repository.py`
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **._persist_stat_field_delta()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_xp()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **test_update_player_stat_field_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_player_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_negative_amount()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_publishes_event()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_delta_type()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_name()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_negative_delta()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- *... and 26 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [ContainerRepository](ContainerRepository.md) (1 shared connections)
- [CreateItemInstanceInput](CreateItemInstanceInput.md) (1 shared connections)
- [PlayerEffectRepository](PlayerEffectRepository.md) (1 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 104 (88%)
- INFERRED: 14 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*