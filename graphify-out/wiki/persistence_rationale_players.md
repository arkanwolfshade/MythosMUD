# persistence rationale players

> 129 nodes

## Key Concepts

- **RoomCacheLoader** (29 connections) — `server/async_persistence_room_loader.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **Any** (19 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **Any** (12 connections)
- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **.load()** (10 connections) — `server/async_persistence_room_loader.py`
- **._generate_room_id_from_zone_data()** (7 connections) — `server/async_persistence_room_loader.py`
- **datetime** (6 connections)
- **._process_combined_rows()** (6 connections) — `server/async_persistence_room_loader.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **Profession** (5 connections)
- **._build_room_data_from_row()** (5 connections) — `server/async_persistence_room_loader.py`
- **._process_exit_rows()** (5 connections) — `server/async_persistence_room_loader.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (4 connections) — `server/async_persistence.py`
- *... and 104 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (51 shared connections)
- [Database Config](Database_Config.md) (17 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [persistence container item](persistence_container_item.md) (1 shared connections)
- [commands recovery lucidity](commands_recovery_lucidity.md) (1 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/async_persistence_room_loader.py`

## Audit Trail

- EXTRACTED: 403 (93%)
- INFERRED: 32 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*