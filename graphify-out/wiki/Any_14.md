# Any

> 73 nodes

## Key Concepts

- **send_game_event()** (30 connections) — `server/realtime/connection_manager_api.py`
- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **connection_manager_api.py** (19 connections) — `server/realtime/connection_manager_api.py`
- **MagicServiceHealingMixin** (15 connections) — `server/game/magic/magic_healing_events.py`
- **magic_healing_events.py** (14 connections) — `server/game/magic/magic_healing_events.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **broadcast_game_event()** (12 connections) — `server/realtime/connection_manager_api.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **__getattr__()** (9 connections) — `server/realtime/connection_manager.py`
- **send_room_event()** (8 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (6 connections)
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **UUID** (6 connections)
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (5 connections)
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- *... and 48 more nodes in this community*

## Relationships

- [message handler factory](message_handler_factory.md) (18 shared connections)
- [Player](Player.md) (11 shared connections)
- [real time](real_time.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)
- [world](world.md) (7 shared connections)
- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (4 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [Protocol](Protocol.md) (3 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [command execution request](command_execution_request.md) (2 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`

## Audit Trail

- EXTRACTED: 301 (91%)
- INFERRED: 29 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*