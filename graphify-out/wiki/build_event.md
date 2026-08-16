# build_event

> 317 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **AttributeError** (45 connections)
- **admin_summon_command.py** (35 connections) — `server/commands/admin_summon_command.py`
- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (30 connections) — `server/realtime/websocket_room_updates.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **test_message_handlers.py** (26 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **asyncio** (24 connections)
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **admin_actions_logger.py** (19 connections) — `server/structured_logging/admin_actions_logger.py`
- **websocket_handler_connection.py** (18 connections) — `server/realtime/websocket_handler_connection.py`
- **message_broadcaster.py** (16 connections) — `server/realtime/messaging/message_broadcaster.py`
- **asyncio** (16 connections)
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **message_handlers.py** (15 connections) — `server/realtime/message_handlers.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- *... and 292 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (44 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (13 shared connections)
- [ConnectionManager](ConnectionManager.md) (13 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (13 shared connections)
- [test_admin_summon_command.py](test_admin_summon_command.py.md) (12 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (10 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (8 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (8 shared connections)
- [connection_manager.py](connection_manager.py.md) (7 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (6 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/commands/admin_setstat_command.py`
- `server/commands/admin_summon_command.py`
- `server/realtime/envelope.py`
- `server/realtime/message_handlers.py`
- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_message_handlers.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`

## Audit Trail

- EXTRACTED: 823 (93%)
- INFERRED: 66 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*