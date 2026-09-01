# test_player_respawn_service.py

> 153 nodes

## Key Concepts

- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (36 connections) — `server/services/player_respawn_service.py`
- **asyncio** (27 connections)
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
- **EncodeLiabilitiesFn** (6 connections) — `server/utils/liability_types.py`
- **._clear_respawn_combat_state()** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (5 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (5 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (5 connections) — `server/services/player_respawn_service.py`
- **._apply_standard_respawn_state()** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (5 connections) — `server/services/player_respawn_service.py`
- *... and 128 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (20 shared connections)
- [Player](Player.md) (14 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (5 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [Stats](Stats.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (3 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 305 (90%)
- INFERRED: 33 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*