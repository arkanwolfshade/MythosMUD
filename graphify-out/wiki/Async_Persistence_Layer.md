# Async Persistence Layer

> 111 nodes · cohesion 0.03

## Key Concepts

- **AsyncPersistenceLayer** (183 connections) — `server/async_persistence.py`
- **Player** (22 connections) — `server/async_persistence.py`
- **UUID** (21 connections) — `server/async_persistence.py`
- **Any** (19 connections) — `server/async_persistence.py`
- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **conftest.py** (5 connections) — `server/tests/unit/infrastructure/conftest.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.apply_corruption()** (4 connections) — `server/async_persistence.py`
- **.apply_fear()** (4 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (4 connections) — `server/async_persistence.py`
- **.async_damage_player()** (4 connections) — `server/async_persistence.py`
- **.async_heal_player()** (4 connections) — `server/async_persistence.py`
- **.create_container()** (4 connections) — `server/async_persistence.py`
- **.damage_player()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- *... and 86 more nodes in this community*

## Relationships

- [[NPC Admin API]] (23 shared connections)
- [[Combat Command Handler]] (15 shared connections)
- [[Game Service Bundle]] (13 shared connections)
- [[Async Persistence Types]] (13 shared connections)
- [[Holiday Persistence Models]] (9 shared connections)
- [[Combat Aggro Threat]] (9 shared connections)
- [[Dependency Injection Tests]] (7 shared connections)
- [[NPC Services Bundle]] (7 shared connections)
- [[Combat Death Handling]] (6 shared connections)
- [[NPC Death Lifecycle]] (5 shared connections)
- [[Async Persistence Core]] (4 shared connections)
- [[Schedule Service Loader]] (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/tests/unit/infrastructure/conftest.py`

## Audit Trail

- EXTRACTED: 413 (82%)
- INFERRED: 92 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
