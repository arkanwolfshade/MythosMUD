# send_game_event

> 41 nodes

## Key Concepts

- **send_game_event()** (28 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (16 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_game_event()** (10 connections) — `server/realtime/connection_manager_api.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **send_player_status_update()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (6 connections) — `server/realtime/connection_manager_api.py`
- **__getattr__()** (5 connections) — `server/realtime/connection_manager.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **UUID** (5 connections)
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_coerce_connection_manager()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **Get MP regeneration multiplier based on player state. Args: stats: Player stats…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- **Restore MP from meditation (highly accelerated regeneration). Args: player_id:…** (1 connections) — `server/game/magic/mp_regeneration_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (11 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [MagicServiceHealingMixin](MagicServiceHealingMixin.md) (1 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)

## Source Files

- `server/game/magic/mp_regeneration_service.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 105 (87%)
- INFERRED: 16 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*