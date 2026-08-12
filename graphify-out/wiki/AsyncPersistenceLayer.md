# AsyncPersistenceLayer

> 175 nodes

## Key Concepts

- **AsyncPersistenceLayer** (163 connections) — `server/async_persistence.py`
- **asyncio** (21 connections)
- **Player** (19 connections)
- **Any** (17 connections)
- **UUID** (15 connections)
- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **infrastructure/conftest.py** (5 connections) — `server/tests/unit/infrastructure/conftest.py`
- **.add_player_effect()** (4 connections) — `server/async_persistence.py`
- **.create_container()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.get_user_by_username_case_insensitive()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **async_persistence_layer()** (4 connections) — `server/tests/unit/infrastructure/conftest.py`
- *... and 150 more nodes in this community*

## Relationships

- [Player](Player.md) (26 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (13 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [combat_service.py](combat_service.py.md) (4 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [test_async_persistence_core.py](test_async_persistence_core.py.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 603 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*