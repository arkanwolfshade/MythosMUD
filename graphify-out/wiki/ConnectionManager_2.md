# ConnectionManager

> God node · 162 connections · `server/realtime/connection_manager.py`

**Community:** [ConnectionManager](ConnectionManager.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`

### contains
- [connection_manager.py](connection_manager.py.md) `EXTRACTED`

### imports
- [server/dependencies.py](server-dependencies.py.md) `EXTRACTED`
- [websocket_handler.py](websocket_handler.py.md) `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- [container_endpoints_basic.py](container_endpoints_basic.py.md) `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- combat_handler.py `EXTRACTED`
- [websocket_initial_state.py](websocket_initial_state.py.md) `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- nats_message_handler.py `EXTRACTED`
- event_handler.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- [websocket_handler_commands.py](websocket_handler_commands.py.md) `EXTRACTED`
- websocket_room_updates.py `EXTRACTED`
- test_envelope.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- api/game.py `EXTRACTED`
- [combat_loader.py](combat_loader.py.md) `EXTRACTED`
- websocket_handler_message_loop.py `EXTRACTED`
- follow_service.py `EXTRACTED`
- event_handlers.py `EXTRACTED`

### method
- .event_bus() `EXTRACTED`
- .check_connection_health() `EXTRACTED`
- ._get_player() `EXTRACTED`
- ._track_player_disconnected() `EXTRACTED`
- .canonical_room_id() `EXTRACTED`
- .connect_websocket() `EXTRACTED`
- .disconnect_websocket() `EXTRACTED`
- .handle_new_game_session() `EXTRACTED`
- .send_personal_message() `EXTRACTED`
- .send_personal_message_old() `EXTRACTED`
- .get_message_delivery_stats() `EXTRACTED`
- .cleanup_dead_connections() `EXTRACTED`
- .broadcast_to_room() `EXTRACTED`
- ._get_players_batch() `EXTRACTED`
- ._track_player_connected() `EXTRACTED`
- ._broadcast_connection_message() `EXTRACTED`
- .detect_and_handle_error_state() `EXTRACTED`
- .handle_websocket_error() `EXTRACTED`
- .handle_authentication_error() `EXTRACTED`
- .handle_security_violation() `EXTRACTED`

### rationale_for
- Manages real-time connections for the game. This refactored version uses… `EXTRACTED`

### references
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- close_container() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _dispatch_player_dp_updated_payload() `EXTRACTED`
- .__init__() `EXTRACTED`
- _connection_manager_from_config_app() `EXTRACTED`
- _npc_died_broadcast_and_bridge() `EXTRACTED`
- _send_combat_participant_updates() `EXTRACTED`
- _send_player_death_notification() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._init_messaging_handlers_and_publisher() `EXTRACTED`
- _publish_npc_died_to_event_bus() `EXTRACTED`
- _refresh_room_after_npc_death() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- [NATSMessageHandler](NATSMessageHandler.md) `INFERRED`
- CombatCommandHandler `INFERRED`
- [RealTimeEventHandler](RealTimeEventHandler.md) `INFERRED`
- FollowService `INFERRED`
- [PartyService](PartyService.md) `INFERRED`
- PlayerRespawnEventHandler `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- RealtimeBundle `INFERRED`
- [EventHandler](EventHandler.md) `INFERRED`
- _NpcWithLife `INFERRED`
- ConnectionMetadata `INFERRED`
- PlayerStateEventHandler `INFERRED`
- RespawnPlayerEventPayload `INFERRED`
- [Party](Party.md) `INFERRED`
- [_EventBusPublishPort](_EventBusPublishPort.md) `INFERRED`
- _NpcLifecycleManagerForOccupants `INFERRED`
- RespawnPlayerStatsPayload `INFERRED`
- AsyncPersistenceRoomLookup `INFERRED`
- PlayerDisconnectService `INFERRED`
- _AppStateForEventHandler `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*