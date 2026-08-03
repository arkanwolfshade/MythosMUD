# persistence rationale players

> 89 nodes

## Key Concepts

- **Player** (22 connections)
- **UUID** (21 connections)
- **Any** (19 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (4 connections) — `server/async_persistence.py`
- **.apply_fear()** (4 connections) — `server/async_persistence.py`
- **.apply_corruption()** (4 connections) — `server/async_persistence.py`
- **.heal_player()** (4 connections) — `server/async_persistence.py`
- **.async_heal_player()** (4 connections) — `server/async_persistence.py`
- **.damage_player()** (4 connections) — `server/async_persistence.py`
- **.async_damage_player()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.create_container()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- **.set_instance_manager()** (3 connections) — `server/async_persistence.py`
- **._load_room_cache_async()** (3 connections) — `server/async_persistence.py`
- *... and 64 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (50 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (3 shared connections)
- [persistence container item](persistence_container_item.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 256 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*