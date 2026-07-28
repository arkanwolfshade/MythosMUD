# Server Infrastructure (4)

> 114 nodes

## Key Concepts

- **AsyncPersistenceLayer** (183 connections) — `server/async_persistence.py`
- **Player** (22 connections)
- **UUID** (21 connections)
- **Any** (19 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **datetime** (6 connections)
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (4 connections) — `server/async_persistence.py`
- **.apply_fear()** (4 connections) — `server/async_persistence.py`
- **.apply_corruption()** (4 connections) — `server/async_persistence.py`
- **.heal_player()** (4 connections) — `server/async_persistence.py`
- **.async_heal_player()** (4 connections) — `server/async_persistence.py`
- **.damage_player()** (4 connections) — `server/async_persistence.py`
- **.async_damage_player()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- *... and 89 more nodes in this community*

## Relationships

- [Server Infrastructure (6)](Server_Infrastructure_%286%29.md) (23 shared connections)
- [Server Admin](Server_Admin.md) (9 shared connections)
- [Server (5)](Server_%285%29.md) (8 shared connections)
- [Server Utils (14)](Server_Utils_%2814%29.md) (8 shared connections)
- [Server Events](Server_Events.md) (7 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (6 shared connections)
- [Server Persistence](Server_Persistence.md) (6 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (6 shared connections)
- [Server Services (36)](Server_Services_%2836%29.md) (6 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (5 shared connections)
- [Server Services (15)](Server_Services_%2815%29.md) (5 shared connections)
- [Server Game (9)](Server_Game_%289%29.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 464 (89%)
- INFERRED: 58 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*