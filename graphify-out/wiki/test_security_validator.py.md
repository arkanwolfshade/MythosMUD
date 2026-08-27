# test_security_validator.py

> 158 nodes

## Key Concepts

- **AsyncPersistenceLayer** (170 connections) — `server/async_persistence.py`
- **movement_service.py** (35 connections) — `server/game/movement_service.py`
- **Player** (20 connections)
- **Any** (17 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **UUID** (15 connections)
- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **Delegate to room loader; exposed for unit tests.** (8 connections) — `server/async_persistence.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **infrastructure/conftest.py** (6 connections) — `server/tests/unit/infrastructure/conftest.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **_apply_physical_strength_bonus()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **_get_target_stats_for_damage()** (5 connections) — `server/services/combat_turn_participant_actions.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **.add_player_effect()** (4 connections) — `server/async_persistence.py`
- **.create_container()** (4 connections) — `server/async_persistence.py`
- *... and 133 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (26 shared connections)
- [NPCDefinition](NPCDefinition.md) (25 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (24 shared connections)
- [ContainerComponent](ContainerComponent.md) (14 shared connections)
- [manager.py](manager.py.md) (14 shared connections)
- [testing_examples.py](testing_examples.py.md) (7 shared connections)
- [ChatService](ChatService.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [map_minimap.py](map_minimap.py.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 386 (91%)
- INFERRED: 37 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*