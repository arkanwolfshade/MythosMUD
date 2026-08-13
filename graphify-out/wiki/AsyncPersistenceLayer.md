# AsyncPersistenceLayer

> 192 nodes

## Key Concepts

- **AsyncPersistenceLayer** (163 connections) — `server/async_persistence.py`
- **movement_service.py** (34 connections) — `server/game/movement_service.py`
- **asyncio** (21 connections)
- **Player** (19 connections)
- **Any** (17 connections)
- **movement_helpers.py** (16 connections) — `server/game/movement_helpers.py`
- **UUID** (15 connections)
- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **validate_player_room_membership()** (8 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (7 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (7 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (6 connections) — `server/game/movement_helpers.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **infrastructure/conftest.py** (5 connections) — `server/tests/unit/infrastructure/conftest.py`
- **.add_player_effect()** (4 connections) — `server/async_persistence.py`
- **.create_container()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- *... and 167 more nodes in this community*

## Relationships

- [log_and_raise](log_and_raise.md) (25 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (12 shared connections)
- [EventBus](EventBus.md) (12 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [._validate_movement](_validate_movement.md) (5 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (4 shared connections)
- [test_async_persistence_core.py](test_async_persistence_core.py.md) (4 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/npc/combat_integration_base.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 419 (96%)
- INFERRED: 17 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*