# Player Movement Service

> 42 nodes · cohesion 0.07

## Key Concepts

- **UUID** (18 connections) — `server/game/movement_service.py`
- **.move_player()** (13 connections) — `server/game/movement_service.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **Room** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._validate_player_room_membership()** (5 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_service.py`
- **.add_player_to_room()** (4 connections) — `server/game/movement_service.py`
- **._check_combat_state()** (4 connections) — `server/game/movement_service.py`
- **._check_player_posture()** (4 connections) — `server/game/movement_service.py`
- **._extract_player_id()** (4 connections) — `server/game/movement_service.py`
- **.get_player_room()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._validate_exit()** (4 connections) — `server/game/movement_service.py`
- **Any** (4 connections) — `server/game/movement_service.py`
- **EventBus** (3 connections) — `server/game/movement_service.py`
- **Resolve player by ID or name and return player object and resolved ID.** (1 connections) — `server/game/movement_service.py`
- **Get and validate rooms for movement.** (1 connections) — `server/game/movement_service.py`
- *... and 17 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (19 shared connections)
- [[NPC Admin API]] (9 shared connections)
- [[Movement Performance Monitor]] (6 shared connections)
- [[Game Service Bundle]] (3 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 143 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
