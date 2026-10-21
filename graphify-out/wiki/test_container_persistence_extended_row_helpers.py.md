# test_container_persistence_extended_row_helpers.py

> 204 nodes · cohesion 0.02

## Key Concepts

- **test_movement_service.py** (72 connections) — `server/tests/unit/game/test_movement_service.py`
- **movement_service.py** (47 connections) — `server/game/movement_service.py`
- **InstanceManager** (41 connections) — `server/game/instance_manager.py`
- **instance_manager.py** (30 connections) — `server/game/instance_manager.py`
- **asyncio** (29 connections)
- **test_instance_manager.py** (25 connections) — `server/tests/unit/game/test_instance_manager.py`
- **instance_flush_service.py** (20 connections) — `server/services/instance_flush_service.py`
- **is_template_room()** (19 connections) — `server/game/instance_manager.py`
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **TemplateRoomEntryError** (15 connections) — `server/game/instance_manager.py`
- **_exit_hook_setup()** (13 connections) — `server/tests/unit/game/test_movement_service.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **.create_instance()** (8 connections) — `server/game/instance_manager.py`
- **Room** (8 connections)
- **template_id_of()** (8 connections) — `server/game/instance_manager.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **template_exit_room_id()** (7 connections) — `server/game/instance_manager.py`
- **instance_manager()** (7 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_template_id_of_and_exit_room()** (7 connections) — `server/tests/unit/game/test_instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (6 connections) — `server/game/instance_manager.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **Room** (6 connections)
- *... and 179 more nodes in this community*

## Relationships

- [_find_item_in_equipped](_find_item_in_equipped.md) (19 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (16 shared connections)
- [Room](Room.md) (12 shared connections)
- [container_helpers_inventory_ops.py](container_helpers_inventory_ops.py.md) (10 shared connections)
- [BaseEvent](BaseEvent.md) (7 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (6 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (6 shared connections)
- [FollowService](FollowService.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (5 shared connections)
- [AttributeError](AttributeError.md) (5 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (4 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (4 shared connections)

## Source Files

- `server/game/instance_manager.py`
- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/game/player_service.py`
- `server/services/instance_flush_service.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 451 (94%)
- INFERRED: 30 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*