# AsyncPersistenceLayer

> 205 nodes

## Key Concepts

- **AsyncPersistenceLayer** (176 connections) — `server/async_persistence.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **asyncio** (23 connections)
- **Player** (19 connections)
- **Any** (17 connections)
- **UUID** (15 connections)
- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (8 connections) — `server/services/combat_death_handler.py`
- **._async_load_from_database()** (7 connections) — `server/services/holiday_service.py`
- **_HolidayLoadResult** (5 connections) — `server/services/holiday_service.py`
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
- *... and 180 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (32 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (23 shared connections)
- [CombatService](CombatService.md) (9 shared connections)
- [container_events.py](container_events.py.md) (8 shared connections)
- [User](User.md) (5 shared connections)
- [HolidayService](HolidayService.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (4 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [ContainerService](ContainerService.md) (4 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (4 shared connections)
- [movement_helpers.py](movement_helpers.py.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/services/combat_death_handler.py`
- `server/services/holiday_service.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 408 (93%)
- INFERRED: 33 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*