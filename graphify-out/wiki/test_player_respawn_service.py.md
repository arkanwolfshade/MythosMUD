# test_player_respawn_service.py

> 159 nodes

## Key Concepts

- **test_player_respawn_service.py** (54 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (36 connections) — `server/services/player_respawn_service.py`
- **asyncio** (27 connections)
- **PlayerDeliriumRespawnedEvent** (16 connections) — `server/events/event_types.py`
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
- *... and 134 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (21 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [Player](Player.md) (12 shared connections)
- [event_handler.py](event_handler.py.md) (9 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (6 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (3 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (2 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 319 (90%)
- INFERRED: 34 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*