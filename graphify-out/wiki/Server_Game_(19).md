# Server Game (19)

> 52 nodes

## Key Concepts

- **MovementService** (40 connections) — `server/game/movement_service.py`
- **UUID** (16 connections)
- **.move_player()** (14 connections) — `server/game/movement_service.py`
- **._validate_movement()** (9 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (8 connections) — `server/game/movement_service.py`
- **.__init__()** (6 connections) — `server/game/magic/spell_effects.py`
- **._validate_move_params()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._validate_player_room_membership()** (6 connections) — `server/game/movement_service.py`
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (6 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (6 connections) — `server/game/movement_service.py`
- **.get_player_room()** (6 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (5 connections) — `server/game/movement_service.py`
- **._check_combat_state()** (5 connections) — `server/game/movement_service.py`
- **._check_player_posture()** (5 connections) — `server/game/movement_service.py`
- **.movement_service()** (4 connections) — `server/game/magic/spell_effects.py`
- **Any** (4 connections)
- **Room** (4 connections)
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._extract_player_id()** (4 connections) — `server/game/movement_service.py`
- *... and 27 more nodes in this community*

## Relationships

- [Server Persistence](Server_Persistence.md) (10 shared connections)
- [Server Utils](Server_Utils.md) (8 shared connections)
- [Server Api](Server_Api.md) (6 shared connections)
- [Server Events](Server_Events.md) (4 shared connections)
- [Server Game (25)](Server_Game_%2825%29.md) (4 shared connections)
- [Server Game (2)](Server_Game_%282%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (2 shared connections)
- [Server Commands (19)](Server_Commands_%2819%29.md) (2 shared connections)
- [Server Api (5)](Server_Api_%285%29.md) (2 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (1 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 204 (92%)
- INFERRED: 17 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*