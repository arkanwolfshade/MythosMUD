# ExperienceRepository

> 49 nodes

## Key Concepts

- **ExperienceRepository** (26 connections) — `server/persistence/repositories/experience_repository.py`
- **experience_repository.py** (19 connections) — `server/persistence/repositories/experience_repository.py`
- **RoomRepository** (16 connections) — `server/persistence/repositories/room_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **asyncio** (10 connections)
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **._persist_stat_field_delta()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_xp()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
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
- **.get_room_by_id()** (2 connections) — `server/persistence/repositories/room_repository.py`
- *... and 24 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (10 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [Player](Player.md) (5 shared connections)
- [get_session_maker](get_session_maker.md) (5 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [async_persistence.py](async_persistence.py.md) (3 shared connections)
- [repositories/__init__.py](repositories-__init__.py.md) (3 shared connections)
- [PlayerStateEventHandler](PlayerStateEventHandler.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [profession_repository.py](profession_repository.py.md) (1 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (1 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 111 (89%)
- INFERRED: 14 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*