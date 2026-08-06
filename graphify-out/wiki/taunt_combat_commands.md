# taunt combat commands

> 132 nodes

## Key Concepts

- **test_movement_service.py** (44 connections) — `server/tests/unit/game/test_movement_service.py`
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
- *... and 107 more nodes in this community*

## Relationships

- [command inventory models](command_inventory_models.md) (13 shared connections)
- [add used user](add_used_user.md) (11 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (3 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [party service game](party_service_game.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 365 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*