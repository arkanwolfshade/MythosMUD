# AsyncPersistenceLayer

> 77 nodes

## Key Concepts

- **AsyncPersistenceLayer** (171 connections) — `server/async_persistence.py`
- **Any** (17 connections)
- **UUID** (15 connections)
- **.add_player_effect()** (4 connections) — `server/async_persistence.py`
- **.create_container()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **.get_user_by_username_case_insensitive()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **test_validate_and_fix_player_room_delegates()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **._build_room_objects()** (3 connections) — `server/async_persistence.py`
- **.create_item_instance()** (3 connections) — `server/async_persistence.py`
- **.delete_player()** (3 connections) — `server/async_persistence.py`
- **.ensure_item_instance()** (3 connections) — `server/async_persistence.py`
- **.get_containers_by_room_id()** (3 connections) — `server/async_persistence.py`
- **.get_player_effect_remaining_ticks()** (3 connections) — `server/async_persistence.py`
- **.has_player_effect()** (3 connections) — `server/async_persistence.py`
- **._parse_exits_json()** (3 connections) — `server/async_persistence.py`
- **._process_combined_rows()** (3 connections) — `server/async_persistence.py`
- **._process_exit_rows()** (3 connections) — `server/async_persistence.py`
- **._process_exits_for_room()** (3 connections) — `server/async_persistence.py`
- **._process_room_rows()** (3 connections) — `server/async_persistence.py`
- **._query_rooms_with_exits_async()** (3 connections) — `server/async_persistence.py`
- *... and 52 more nodes in this community*

## Relationships

- [Player](Player.md) (25 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (24 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [pytest.md](pytest.md.md) (6 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [models/container.py](models-container.py.md) (4 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (4 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 211 (84%)
- INFERRED: 39 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*