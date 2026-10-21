# _find_item_in_equipped

> 48 nodes · cohesion 0.07

## Key Concepts

- **MovementService** (47 connections) — `server/game/movement_service.py`
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **UUID** (13 connections)
- **.move_player()** (8 connections) — `server/game/movement_service.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (7 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (6 connections) — `server/game/movement_service.py`
- **.__init__()** (6 connections) — `server/game/movement_service.py`
- **._maybe_trigger_room_entry_hallucination()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **test_movement_service_init()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init_no_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_room_transfer_tells_the_source_room_where_the_player_went()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **.set_player_combat_service()** (2 connections) — `server/game/movement_service.py`
- **Room** (2 connections)
- *... and 23 more nodes in this community*

## Relationships

- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (19 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (2 shared connections)
- [.initialize](initialize.md) (2 shared connections)
- [_CombatServiceDeps](_CombatServiceDeps.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [endpoints.py](endpoints.py.md) (2 shared connections)
- [test_process_mortally_wounded_tick_changes_posture_to_lying](test_process_mortally_wounded_tick_changes_posture_to_lying.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 118 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*