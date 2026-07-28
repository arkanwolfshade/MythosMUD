# Server Realtime (48)

> 45 nodes

## Key Concepts

- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_api.py** (16 connections) — `server/realtime/connection_manager_api.py`
- **MagicServiceHealingMixin** (15 connections) — `server/game/magic/magic_healing_events.py`
- **connection_manager_utils.py** (15 connections) — `server/realtime/connection_manager_utils.py`
- **magic_healing_events.py** (14 connections) — `server/game/magic/magic_healing_events.py`
- **resolve_connection_manager()** (14 connections) — `server/realtime/connection_manager_utils.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **lazy_import_api_function()** (11 connections) — `server/realtime/connection_manager_utils.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **send_room_event()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (6 connections)
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (5 connections)
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (5 connections)
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **_coerce_connection_manager()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_make_async_compat_wrapper()** (3 connections) — `server/realtime/connection_manager_utils.py`
- **Healing event notification for spellcasting.  Mixin that sends player_dp_updated** (1 connections) — `server/game/magic/magic_healing_events.py`
- *... and 20 more nodes in this community*

## Relationships

- [Server Persistence](Server_Persistence.md) (7 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (6 shared connections)
- [Server App](Server_App.md) (4 shared connections)
- [Server Events](Server_Events.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (4 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (4 shared connections)
- [Server Models (13)](Server_Models_%2813%29.md) (3 shared connections)
- [Server App (3)](Server_App_%283%29.md) (3 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (3 shared connections)
- [Server Game (20)](Server_Game_%2820%29.md) (3 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (3 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 198 (84%)
- INFERRED: 37 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*