# message nats handler

> 52 nodes

## Key Concepts

- **MovementService** (43 connections) — `server/game/movement_service.py`
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
- **.__init__()** (5 connections) — `server/game/movement_service.py`
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
- *... and 27 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (18 shared connections)
- [Loot Generation](Loot_Generation.md) (8 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [party service game](party_service_game.md) (3 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)
- [movement service game](movement_service_game.md) (2 shared connections)
- [events event bus](events_event_bus.md) (2 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [retry nats handler](retry_nats_handler.md) (1 shared connections)
- [spell game magic](spell_game_magic.md) (1 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 203 (91%)
- INFERRED: 19 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*