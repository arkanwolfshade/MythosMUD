# movement service game

> 94 nodes

## Key Concepts

- **MovementService** (43 connections) — `server/game/movement_service.py`
- **test_movement_service.py** (25 connections) — `server/tests/unit/game/test_movement_service.py`
- **UUID** (16 connections)
- **.move_player()** (14 connections) — `server/game/movement_service.py`
- **._validate_movement()** (9 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (8 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._validate_player_room_membership()** (6 connections) — `server/game/movement_service.py`
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (6 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (6 connections) — `server/game/movement_service.py`
- **.get_player_room()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (5 connections) — `server/game/movement_service.py`
- **._check_combat_state()** (5 connections) — `server/game/movement_service.py`
- **._check_player_posture()** (5 connections) — `server/game/movement_service.py`
- **Any** (4 connections)
- **Room** (4 connections)
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._extract_player_id()** (4 connections) — `server/game/movement_service.py`
- **._validate_exit()** (4 connections) — `server/game/movement_service.py`
- **.get_room_players()** (4 connections) — `server/game/movement_service.py`
- *... and 69 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (12 shared connections)
- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [npc populate databases](npc_populate_databases.md) (10 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (8 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)
- [spell game magic](spell_game_magic.md) (2 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [spell models rationale](spell_models_rationale.md) (1 shared connections)
- [magic healing game](magic_healing_game.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 289 (93%)
- INFERRED: 22 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*