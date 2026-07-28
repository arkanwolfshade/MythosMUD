# ConnectionManager

> God node · 172 connections · `server/realtime/connection_manager.py`

**Community:** [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md)

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
- event_handler.py `EXTRACTED`
- nats_message_handler.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- websocket_room_updates.py `EXTRACTED`
- test_envelope.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- game.py `EXTRACTED`
- combat_loader.py `EXTRACTED`
- websocket_handler_message_loop.py `EXTRACTED`
- follow_service.py `EXTRACTED`

### indirect_call
- _coerce_connection_manager() `INFERRED`
- test_build_event_sequence_priority() `INFERRED`
- test_build_event_with_connection_manager() `INFERRED`
- mock_connection_manager() `INFERRED`

### method
- .__init__() `EXTRACTED`
- .event_bus() `EXTRACTED`
- .check_connection_health() `EXTRACTED`
- ._get_player() `EXTRACTED`
- ._track_player_disconnected() `EXTRACTED`
- ._broadcast_connection_message() `EXTRACTED`
- .broadcast_to_room() `EXTRACTED`
- .canonical_room_id() `EXTRACTED`
- .cleanup_dead_connections() `EXTRACTED`
- .connect_websocket() `EXTRACTED`
- .detect_and_handle_error_state() `EXTRACTED`
- .disconnect_websocket() `EXTRACTED`
- .get_message_delivery_stats() `EXTRACTED`
- .get_pending_messages() `EXTRACTED`
- .get_player_presence_info() `EXTRACTED`
- ._get_players_batch() `EXTRACTED`
- .get_rate_limit_info() `EXTRACTED`
- .handle_authentication_error() `EXTRACTED`
- .handle_new_game_session() `EXTRACTED`
- .handle_security_violation() `EXTRACTED`

### rationale_for
- Manages real-time connections for the game.      This refactored version uses mo `EXTRACTED`

### references
- loot_all_items() `EXTRACTED`
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- close_container() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _dispatch_player_dp_updated_payload() `EXTRACTED`
- _send_combat_participant_updates() `EXTRACTED`
- _connection_manager_from_config_app() `EXTRACTED`
- _npc_died_broadcast_and_bridge() `EXTRACTED`
- _publish_npc_died_to_event_bus() `EXTRACTED`
- _send_player_death_notification() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._init_messaging_handlers_and_publisher() `EXTRACTED`
- _refresh_room_after_npc_death() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- RateLimiter `INFERRED`
- CombatCommandHandler `INFERRED`
- MessageQueue `INFERRED`
- RoomSubscriptionManager `INFERRED`
- RealTimeEventHandler `INFERRED`
- FollowService `INFERRED`
- PartyService `INFERRED`
- PlayerRespawnEventHandler `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- NATSMessageHandler `INFERRED`
- EventHandler `INFERRED`
- _NpcWithLife `INFERRED`
- RealtimeBundle `INFERRED`
- ConnectionMetadata `INFERRED`
- MemoryMonitor `INFERRED`
- PlayerStateEventHandler `INFERRED`
- RespawnPlayerEventPayload `INFERRED`
- Party `INFERRED`
- _EventBusPublishPort `INFERRED`
- _AppWithState `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*