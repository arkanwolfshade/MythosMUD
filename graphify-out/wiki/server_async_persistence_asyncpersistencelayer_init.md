# server async persistence asyncpersistencelayer init

> 53 nodes

## Key Concepts

- **player_effect_repository.py** (22 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **RoomRepository** (16 connections) — `server/persistence/repositories/room_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **.get_active_effects_for_player()** (9 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.add_effect()** (7 connections) — `server/persistence/repositories/player_effect_repository.py`
- **UUID** (7 connections)
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Any** (6 connections)
- **AddEffectInput** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.delete_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.has_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_str_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._remaining_ticks()** (3 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **.get_room_by_id()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.list_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_room()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- *... and 28 more nodes in this community*

## Relationships

- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (21 shared connections)
- [fixturerequest](fixturerequest.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server async persistence](server_async_persistence.md) (3 shared connections)
- [server async persistence asyncpersistencelayer create](server_async_persistence_asyncpersistencelayer_create.md) (2 shared connections)
- [server game mechanics gamemechanicsservice](server_game_mechanics_gamemechanicsservice.md) (1 shared connections)
- [server persistence container create params](server_persistence_container_create_params.md) (1 shared connections)
- [server async persistence room loader](server_async_persistence_room_loader.md) (1 shared connections)
- [moduletype](moduletype.md) (1 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 120 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*