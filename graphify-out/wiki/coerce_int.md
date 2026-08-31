# coerce_int

> 54 nodes

## Key Concepts

- **coerce_int()** (51 connections) — `server/utils/int_coercion.py`
- **player_event_handlers_respawn.py** (35 connections) — `server/realtime/player_event_handlers_respawn.py`
- **int_coercion.py** (17 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **test_inventory_command_coercion.py** (13 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **_append_unique_valid_occupant()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_ensure_respawned_player_in_lists()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_is_npc_occupant_row()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_occupant_str_field()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_coerce_int_string_parsing()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_stats_int_delegates_to_coerce_int()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_bool_before_int()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **test_coerce_int_float()** (2 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- *... and 29 more nodes in this community*

## Relationships

- [Player](Player.md) (16 shared connections)
- [LucidityService](LucidityService.md) (9 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (7 shared connections)
- [RespawnPlayerEventPayload](RespawnPlayerEventPayload.md) (7 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (7 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (6 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (5 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (5 shared connections)
- [test_look_container_helpers.py](test_look_container_helpers.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (2 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)

## Source Files

- `server/models/player.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 166 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*