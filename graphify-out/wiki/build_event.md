# build_event

> 206 nodes

## Key Concepts

- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (34 connections) — `server/realtime/websocket_room_updates.py`
- **envelope.py** (32 connections) — `server/realtime/envelope.py`
- **broadcast_room_update()** (31 connections) — `server/realtime/websocket_room_updates.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **asyncio** (21 connections)
- **.connection_manager()** (13 connections) — `server/services/combat_messaging/base.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **log_room_broadcast_result()** (12 connections) — `server/services/combat_messaging/base.py`
- **combat_messaging/base.py** (12 connections) — `server/services/combat_messaging/base.py`
- **test_websocket_room_updates_fanout.py** (12 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **CombatBroadcastMixin** (11 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **get_npc_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **PlayerBroadcastMixin** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_broadcasts.py** (10 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **player_broadcasts.py** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **_looks_like_player_uuid()** (8 connections) — `server/realtime/websocket_room_updates.py`
- **test_broadcast_room_update_personalizes_for_hallucinating_viewer()** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **.broadcast_combat_attack()** (7 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- *... and 181 more nodes in this community*

## Relationships

- [game_state_provider.py](game_state_provider.py.md) (19 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (10 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (7 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (7 shared connections)
- [EventHandler](EventHandler.md) (5 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (5 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (4 shared connections)
- [test_admin_commands_helpers.py](test_admin_commands_helpers.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (4 shared connections)
- [send_game_event](send_game_event.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`

## Audit Trail

- EXTRACTED: 512 (96%)
- INFERRED: 22 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*