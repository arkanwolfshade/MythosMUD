# build_event

> 114 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging/base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **Any** (7 connections)
- **HasConnectionManager** (6 connections) — `server/services/combat_messaging/base.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **.broadcast_combat_death()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_end()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_error()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_combat_start()** (4 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- *... and 89 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (29 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (10 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (5 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (4 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (4 shared connections)
- [AttributeError](AttributeError.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [TestCombatMessagingService](TestCombatMessagingService.md) (3 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (3 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (3 shared connections)
- [position_commands.py](position_commands.py.md) (3 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 298 (96%)
- INFERRED: 13 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*