# ConnectionManager

> God node · 233 connections · `server/realtime/connection_manager.py`

**Community:** [Room Broadcast](Room_Broadcast.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`

### contains
- connection_manager.py `EXTRACTED`

### imports
- dependencies.py `EXTRACTED`
- websocket_handler.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- websocket_room_updates.py `EXTRACTED`
- event_handler.py `EXTRACTED`
- nats_message_handler.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- test_envelope.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- combat_loader.py `EXTRACTED`
- websocket_handler_message_loop.py `EXTRACTED`
- game.py `EXTRACTED`
- follow_service.py `EXTRACTED`

### indirect_call
- test_build_event_sequence_priority() `INFERRED`
- test_build_event_with_connection_manager() `INFERRED`
- mock_connection_manager() `INFERRED`

### method
- .event_bus() `EXTRACTED`
- .__init__() `EXTRACTED`
- .check_connection_health() `EXTRACTED`
- ._get_player() `EXTRACTED`
- ._track_player_disconnected() `EXTRACTED`
- ._broadcast_connection_message() `EXTRACTED`
- .canonical_room_id() `EXTRACTED`
- .connect_websocket() `EXTRACTED`
- .disconnect_websocket() `EXTRACTED`
- ._get_players_batch() `EXTRACTED`
- ._send_initial_game_state() `EXTRACTED`
- ._track_player_connected() `EXTRACTED`
- .broadcast_to_room() `EXTRACTED`
- ._check_and_process_disconnect() `EXTRACTED`
- .cleanup_dead_connections() `EXTRACTED`
- ._cleanup_dead_websocket() `EXTRACTED`
- .detect_and_handle_error_state() `EXTRACTED`
- .disconnect_websocket_connection() `EXTRACTED`
- .force_disconnect_player() `EXTRACTED`
- .get_connection_count() `EXTRACTED`

### rationale_for
- Manages real-time connections for the game.      This refactored version uses mo `EXTRACTED`

### references
- loot_all_items() `EXTRACTED`
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- close_container() `EXTRACTED`
- resolve_connection_manager() `EXTRACTED`
- force_disconnect_player_impl() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- safe_close_websocket_impl() `EXTRACTED`
- _send_combat_participant_updates() `EXTRACTED`
- _dispatch_player_dp_updated_payload() `EXTRACTED`
- broadcast_global_event_impl() `EXTRACTED`
- broadcast_room_event_impl() `EXTRACTED`
- broadcast_to_room_impl() `EXTRACTED`
- get_player_impl() `EXTRACTED`
- get_players_batch_impl() `EXTRACTED`
- send_initial_game_state_impl() `EXTRACTED`
- _connection_manager_from_config_app() `EXTRACTED`
- broadcast_global_impl() `EXTRACTED`

### uses
- RateLimiter `INFERRED`
- CombatCommandHandler `INFERRED`
- MessageQueue `INFERRED`
- RoomSubscriptionManager `INFERRED`
- RealTimeEventHandler `INFERRED`
- FollowService `INFERRED`
- PartyService `INFERRED`
- EventHandler `INFERRED`
- PlayerRespawnEventHandler `INFERRED`
- EventPublisher `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- RealtimeBundle `INFERRED`
- NATSMessageHandler `INFERRED`
- ConnectionMetadata `INFERRED`
- _NpcWithLife `INFERRED`
- PlayerStateEventHandler `INFERRED`
- RespawnPlayerEventPayload `INFERRED`
- Party `INFERRED`
- _EventBusPublishPort `INFERRED`
- _AppWithState `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*