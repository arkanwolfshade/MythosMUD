# movement service game

> 10 nodes

## Key Concepts

- **test_movement_service.py** (44 connections) — `server/tests/unit/game/test_movement_service.py`
- **movement_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_player_location_true()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_validate_move_params_same_room()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_check_player_posture_blocks_sitting()** (2 connections) — `server/tests/unit/game/test_movement_service.py`
- **Unit tests for movement service.  Tests the MovementService class.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Create a MovementService instance.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test validate_player_location() returns True when player is in room.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test _validate_move_params returns False for same room.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test _check_player_posture blocks non-standing posture.** (1 connections) — `server/tests/unit/game/test_movement_service.py`

## Relationships

- [game room service](game_room_service.md) (7 shared connections)
- [event bus events](event_bus_events.md) (7 shared connections)
- [events event bus](events_event_bus.md) (5 shared connections)
- [realtime player event](realtime_player_event.md) (4 shared connections)
- [message nats handler](message_nats_handler.md) (2 shared connections)
- [realtime npc event](realtime_npc_event.md) (2 shared connections)
- [player realtime event](player_realtime_event.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [subzone realtime nats](subzone_realtime_nats.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)
- [models profession repr](models_profession_repr.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*