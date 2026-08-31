# PlayerRespawnService

> 55 nodes

## Key Concepts

- **PlayerRespawnService** (36 connections) — `server/services/player_respawn_service.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (13 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **Player** (8 connections)
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (7 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **._clear_respawn_combat_state()** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (5 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (5 connections) — `server/services/player_respawn_service.py`
- **._apply_standard_respawn_state()** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_delirium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_sanitarium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_standard_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **.move_player_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **._publish_delirium_respawn_event()** (5 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_player_state()** (4 connections) — `server/services/player_respawn_service.py`
- **.__init__()** (4 connections) — `server/services/player_respawn_service.py`
- **.clear_player_combat_state()** (3 connections) — `server/services/player_respawn_service.py`
- *... and 30 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (15 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (7 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 127 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*