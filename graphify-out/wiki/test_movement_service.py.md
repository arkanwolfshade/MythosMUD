# test_movement_service.py

> 169 nodes

## Key Concepts

- **test_movement_service.py** (54 connections) — `server/tests/unit/game/test_movement_service.py`
- **MovementService** (51 connections) — `server/game/movement_service.py`
- **movement_service.py** (38 connections) — `server/game/movement_service.py`
- **asyncio** (23 connections)
- **UUID** (19 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **.move_player()** (8 connections) — `server/game/movement_service.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._maybe_trigger_room_entry_hallucination()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- *... and 144 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (28 shared connections)
- [FollowService](FollowService.md) (7 shared connections)
- [event_types.py](event_types.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (4 shared connections)
- [test_go_command.py](test_go_command.py.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (2 shared connections)
- [admin_hallucinate_command.py](admin_hallucinate_command.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 339 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*