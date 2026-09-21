# MovementService

> 26 nodes

## Key Concepts

- **MovementService** (51 connections) — `server/game/movement_service.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **.movement_service()** (4 connections) — `server/game/magic/spell_effects.py`
- **.get_room_players()** (3 connections) — `server/game/movement_service.py`
- **.validate_player_location()** (3 connections) — `server/game/movement_service.py`
- **test_movement_service_init()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init_no_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **.set_player_combat_service()** (2 connections) — `server/game/movement_service.py`
- **Movement service for flee effect.** (1 connections) — `server/game/magic/spell_effects.py`
- **Service for handling atomic player movement operations. This class provides…** (1 connections) — `server/game/movement_service.py`
- **Load fresh player from persistence for posture check when available.** (1 connections) — `server/game/movement_service.py`
- **Validate rooms, membership, and exit for movement.** (1 connections) — `server/game/movement_service.py`
- **Validate that a movement operation is allowed. Args: player_obj: The player…** (1 connections) — `server/game/movement_service.py`
- **Validate parameters for remove_player_from_room operation.** (1 connections) — `server/game/movement_service.py`
- **Remove a player from a room (for logout, teleportation, etc.). Args: player_id:…** (1 connections) — `server/game/movement_service.py`
- **Get all players currently in a room. Args: room_id: The ID of the room to check…** (1 connections) — `server/game/movement_service.py`
- **Validate that a player is in the specified room. Args: player_id: The ID of the…** (1 connections) — `server/game/movement_service.py`
- **Set the player combat service after initialization. This allows the combat…** (1 connections) — `server/game/movement_service.py`
- **Initialize NPC movement integration. Args: event_bus: Optional EventBus…** (1 connections) — `server/npc/movement_integration.py`
- **Test MovementService initialization without persistence raises error.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 1 more nodes in this community*

## Relationships

- [UUID](UUID.md) (14 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (13 shared connections)
- [._execute_move_locked](_execute_move_locked.md) (10 shared connections)
- [follow_service.py](follow_service.py.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [spell_effects.py](spell_effects.py.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [FollowService](FollowService.md) (1 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/game/movement_service.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 79 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*