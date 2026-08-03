# player room persistence

> 60 nodes

## Key Concepts

- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Player** (13 connections)
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **UUID** (7 connections)
- **.update_player_last_active()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository_room.py** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room_with_persistence()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.soft_delete_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.delete_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **Any** (5 connections)
- **should_skip_room_validation()** (5 connections) — `server/persistence/repositories/player_repository_room.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **_coerce_row_stats()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- *... and 35 more nodes in this community*

## Relationships

- [npc populate databases](npc_populate_databases.md) (19 shared connections)
- [Database Config](Database_Config.md) (13 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (13 shared connections)
- [world models rationale](world_models_rationale.md) (9 shared connections)
- [player persistence repository](player_persistence_repository.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (5 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (4 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [dialogue definitions admin](dialogue_definitions_admin.md) (2 shared connections)
- [retry rationale transient()](retry_rationale_transient%28%29.md) (2 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_room.py`

## Audit Trail

- EXTRACTED: 271 (93%)
- INFERRED: 20 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*