# Room Map Viewer UI

> 69 nodes

## Key Concepts

- **MovementService** (45 connections) — `server/game/movement_service.py`
- **UUID** (18 connections)
- **movement_helpers.py** (16 connections) — `server/game/movement_helpers.py`
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **validate_player_room_membership()** (9 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (8 connections) — `server/game/movement_helpers.py`
- **._handle_movement_error()** (8 connections) — `server/game/movement_service.py`
- **.move_player()** (8 connections) — `server/game/movement_service.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **check_player_posture()** (7 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (7 connections) — `server/game/movement_helpers.py`
- **Any** (7 connections)
- **.add_player_to_room()** (7 connections) — `server/game/movement_service.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **._validate_move_params()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (6 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (6 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (6 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (6 connections) — `server/game/movement_service.py`
- **.get_player_room()** (6 connections) — `server/game/movement_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- *... and 44 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (21 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (21 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (8 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (4 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (2 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)
- [Player Respawn Handlers](Player_Respawn_Handlers.md) (1 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)

## Source Files

- `server/game/movement_helpers.py`
- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 288 (94%)
- INFERRED: 20 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*