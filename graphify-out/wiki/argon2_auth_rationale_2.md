# argon2 auth rationale

> 52 nodes

## Key Concepts

- **__init__.py** (30 connections) — `server/persistence/repositories/__init__.py`
- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **RoomRepository** (17 connections) — `server/persistence/repositories/room_repository.py`
- **experience_repository.py** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **room_repository.py** (8 connections) — `server/persistence/repositories/room_repository.py`
- **.update_player_xp()** (7 connections) — `server/persistence/repositories/experience_repository.py`
- **test_room_repository.py** (7 connections) — `server/tests/unit/persistence/test_room_repository.py`
- **.gain_experience()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **UUID** (5 connections)
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/room_repository.py`
- **test_update_player_xp_player_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **Any** (2 connections)
- **Player** (2 connections)
- **.get_room_by_id()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.list_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_room()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **.save_rooms()** (2 connections) — `server/persistence/repositories/room_repository.py`
- **repo()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_negative_amount()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_success()** (2 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- *... and 27 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (22 shared connections)
- [NPC Combat](NPC_Combat.md) (8 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [persistence container item](persistence_container_item.md) (6 shared connections)
- [combat models rationale](combat_models_rationale.md) (5 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (3 shared connections)
- [command commands service](command_commands_service.md) (3 shared connections)
- [effect player repository](effect_player_repository.md) (3 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/room_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`
- `server/tests/unit/persistence/test_room_repository.py`

## Audit Trail

- EXTRACTED: 215 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*