# Server Realtime (2)

> 182 nodes

## Key Concepts

- **build_event()** (113 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **_send_combat_participant_updates()** (8 connections) — `server/realtime/event_handlers.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **_EventBusPublishPort** (7 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (7 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- **Any** (7 connections)
- *... and 157 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (24 shared connections)
- [Server Events](Server_Events.md) (21 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (14 shared connections)
- [Server Realtime](Server_Realtime.md) (10 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (9 shared connections)
- [Server Realtime (9)](Server_Realtime_%289%29.md) (6 shared connections)
- [Server Realtime (14)](Server_Realtime_%2814%29.md) (6 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (6 shared connections)
- [Server Realtime (43)](Server_Realtime_%2843%29.md) (5 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (5 shared connections)
- [Server Realtime (35)](Server_Realtime_%2835%29.md) (5 shared connections)
- [Server Commands (63)](Server_Commands_%2863%29.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/integration/game_state_provider.py`
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

- EXTRACTED: 727 (96%)
- INFERRED: 28 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*