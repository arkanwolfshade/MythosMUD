# combat services messaging

> 150 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- **Any** (7 connections)
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **CombatMessages** (6 connections)
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- *... and 125 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (9 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (6 shared connections)
- [schedule services service](schedule_services_service.md) (6 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (5 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (4 shared connections)
- [instance game manager](instance_game_manager.md) (4 shared connections)
- [combat configuration service](combat_configuration_service.md) (4 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (4 shared connections)
- [command models moderation](command_models_moderation.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_messaging_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 601 (97%)
- INFERRED: 21 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*