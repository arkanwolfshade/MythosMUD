# PlayerRespawnService

> 78 nodes

## Key Concepts

- **PlayerRespawnService** (36 connections) — `server/services/player_respawn_service.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (13 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_liability_update()** (11 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **Player** (8 connections)
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (7 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **fixture** (7 connections)
- **DecodeLiabilitiesFn** (6 connections) — `server/utils/liability_types.py`
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
- *... and 53 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (23 shared connections)
- [LucidityService](LucidityService.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [Player](Player.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (1 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 163 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*