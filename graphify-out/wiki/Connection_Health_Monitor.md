# Connection Health Monitor

> 51 nodes

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
- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **UUID** (5 connections)
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **_coerce_connection_manager()** (4 connections) — `server/realtime/connection_manager_utils.py`
- **_ensure_async_compat()** (4 connections) — `server/realtime/connection_manager_utils.py`
- *... and 26 more nodes in this community*

## Relationships

- [Application DI Bundles](Application_DI_Bundles.md) (10 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (4 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (4 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (3 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (3 shared connections)
- [Combat Messaging Base](Combat_Messaging_Base.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (2 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/spell_costs.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 213 (85%)
- INFERRED: 37 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*