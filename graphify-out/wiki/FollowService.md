# FollowService

> 112 nodes · cohesion 0.03

## Key Concepts

- **coerce_int()** (70 connections) — `server/utils/int_coercion.py`
- **player_respawn_service.py** (51 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (33 connections) — `server/services/player_respawn_service.py`
- **int_coercion.py** (26 connections) — `server/utils/int_coercion.py`
- **player_respawn_state.py** (22 connections) — `server/services/player_respawn_state.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **UUID** (14 connections)
- **._prepare_sanitarium_respawn()** (13 connections) — `server/services/player_respawn_service.py`
- **test_inventory_command_coercion.py** (12 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **._apply_sanitarium_liability_update()** (11 connections) — `server/services/player_respawn_service.py`
- **test_player_respawn_death_room.py** (10 connections) — `server/tests/unit/services/test_player_respawn_death_room.py`
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **record_death_room_on_player()** (9 connections) — `server/services/player_respawn_state.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **apply_standard_respawn_state()** (7 connections) — `server/services/player_respawn_state.py`
- **Player** (7 connections)
- **_player_with_stats()** (7 connections) — `server/tests/unit/services/test_player_respawn_death_room.py`
- **._clear_respawn_combat_state()** (6 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (6 connections) — `server/services/player_respawn_service.py`
- **.move_player_to_limbo()** (6 connections) — `server/services/player_respawn_service.py`
- *... and 87 more nodes in this community*

## Relationships

- [PopulationStats](PopulationStats.md) (20 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (13 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (13 shared connections)
- [ui-v2/types.ts](ui-v2-types.ts.md) (11 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [Room](Room.md) (6 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (6 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (6 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (5 shared connections)
- [BaseEvent](BaseEvent.md) (5 shared connections)
- [look_helpers.py](look_helpers.py.md) (5 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)

## Source Files

- `server/models/player.py`
- `server/services/player_respawn_service.py`
- `server/services/player_respawn_state.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/tests/unit/services/test_player_respawn_death_room.py`
- `server/utils/int_coercion.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 348 (95%)
- INFERRED: 18 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*