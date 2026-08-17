# build_event

> 259 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **PlayerPositionService** (48 connections) — `server/services/player_position_service.py`
- **websocket_room_updates.py** (30 connections) — `server/realtime/websocket_room_updates.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_login_grace_period_visual_indicator.py** (29 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **test_player_position_service.py** (28 connections) — `server/tests/unit/services/test_player_position_service.py`
- **position_commands.py** (27 connections) — `server/commands/position_commands.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **player_position_service.py** (17 connections) — `server/services/player_position_service.py`
- **test_lifespan_event_subscriptions.py** (17 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **lifespan_event_subscriptions.py** (14 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **asyncio** (12 connections)
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- *... and 234 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (61 shared connections)
- [get_logger](get_logger.md) (33 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (29 shared connections)
- [AliasStorage](AliasStorage.md) (25 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (13 shared connections)
- [.change_position](change_position.md) (12 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (11 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (9 shared connections)
- [DatabaseError](DatabaseError.md) (9 shared connections)
- [Any](Any.md) (8 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (7 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/commands/admin_setstat_command.py`
- `server/commands/position_commands.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_manager.py`
- `server/realtime/envelope.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_service.py`
- `server/services/player_position_service.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 730 (93%)
- INFERRED: 54 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*