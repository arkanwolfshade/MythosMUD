# send_game_event

> 63 nodes

## Key Concepts

- **send_game_event()** (28 connections) — `server/realtime/connection_manager_api.py`
- **MPRegenerationService** (19 connections) — `server/game/magic/mp_regeneration_service.py`
- **connection_manager_api.py** (16 connections) — `server/realtime/connection_manager_api.py`
- **MagicServiceHealingMixin** (15 connections) — `server/game/magic/magic_healing_events.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **magic_healing_events.py** (14 connections) — `server/game/magic/magic_healing_events.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_game_event()** (10 connections) — `server/realtime/connection_manager_api.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **send_player_status_update()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_event()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (6 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (6 connections)
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (5 connections)
- **Any** (5 connections)
- **UUID** (5 connections)
- **UUID** (5 connections)
- *... and 38 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [magic_service.py](magic_service.py.md) (11 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [Spell](Spell.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [ScheduleService](ScheduleService.md) (3 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (2 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 269 (89%)
- INFERRED: 32 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*