# Player Movement Service

> 88 nodes · cohesion 0.03

## Key Concepts

- **MovementService** (43 connections) — `server/game/movement_service.py`
- **test_movement_service.py** (25 connections) — `server/tests/unit/game/test_movement_service.py`
- **UUID** (16 connections)
- **.move_player()** (14 connections) — `server/game/movement_service.py`
- **._validate_movement()** (9 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (8 connections) — `server/game/movement_service.py`
- **.get_player_room()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (6 connections) — `server/game/movement_service.py`
- **._validate_player_room_membership()** (6 connections) — `server/game/movement_service.py`
- **._check_combat_state()** (5 connections) — `server/game/movement_service.py`
- **._check_player_posture()** (5 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (5 connections) — `server/game/movement_service.py`
- **._extract_player_id()** (4 connections) — `server/game/movement_service.py`
- **.get_room_players()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._validate_exit()** (4 connections) — `server/game/movement_service.py`
- **.validate_player_location()** (4 connections) — `server/game/movement_service.py`
- **Any** (4 connections)
- **Room** (4 connections)
- **movement_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_move_player_empty_player_id()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- *... and 63 more nodes in this community*

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (19 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (10 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (8 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (3 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (2 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (2 shared connections)
- [Map Editing Hooks](Map_Editing_Hooks.md) (1 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 272 (94%)
- INFERRED: 18 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*