# ConnectionManager

> God node · 228 connections · `server/realtime/connection_manager.py`

**Community:** [[Room Occupant Events]]

## Connections by Relation

### calls
- [[.initialize()]] `EXTRACTED`

### contains
- [[connection_manager.py]] `EXTRACTED`

### imports
- [[dependencies.py]] `EXTRACTED`
- [[websocket_handler.py]] `EXTRACTED`
- [[container_endpoints_basic.py]] `EXTRACTED`
- [[websocket_initial_state.py]] `EXTRACTED`
- [[npc_combat_integration_service.py]] `EXTRACTED`
- [[test_websocket_initial_state.py]] `EXTRACTED`
- [[inventory_command_helpers.py]] `EXTRACTED`
- [[nats_message_handler.py]] `EXTRACTED`
- [[container_endpoints_loot.py]] `EXTRACTED`
- [[event_handler.py]] `EXTRACTED`
- [[player_event_handlers_respawn.py]] `EXTRACTED`
- [[websocket_handler_commands.py]] `EXTRACTED`
- [[websocket_room_updates.py]] `EXTRACTED`
- [[combat_handler.py]] `EXTRACTED`
- [[test_envelope.py]] `EXTRACTED`
- [[websocket_handler_message_loop.py]] `EXTRACTED`
- [[game.py]] `EXTRACTED`
- [[player_disconnect_handlers.py]] `EXTRACTED`
- [[player_event_handlers_state.py]] `EXTRACTED`
- [[event_handlers.py]] `EXTRACTED`

### method
- [[.__init__()]] `EXTRACTED`
- [[.check_connection_health()]] `EXTRACTED`
- [[._track_player_disconnected()]] `EXTRACTED`
- [[._broadcast_connection_message()]] `EXTRACTED`
- [[.broadcast_to_room()]] `EXTRACTED`
- [[.canonical_room_id()]] `EXTRACTED`
- [[.cleanup_dead_connections()]] `EXTRACTED`
- [[.connect_websocket()]] `EXTRACTED`
- [[.detect_and_handle_error_state()]] `EXTRACTED`
- [[.disconnect_websocket()]] `EXTRACTED`
- [[.get_message_delivery_stats()]] `EXTRACTED`
- [[.get_pending_messages()]] `EXTRACTED`
- [[._get_player()]] `EXTRACTED`
- [[.get_player_presence_info()]] `EXTRACTED`
- [[._get_players_batch()]] `EXTRACTED`
- [[.get_rate_limit_info()]] `EXTRACTED`
- [[.handle_authentication_error()]] `EXTRACTED`
- [[.handle_new_game_session()]] `EXTRACTED`
- [[.handle_security_violation()]] `EXTRACTED`
- [[.handle_websocket_error()]] `EXTRACTED`

### rationale_for
- [[Manages real-time connections for the game.      This refactored version uses mo]] `EXTRACTED`

### uses
- [[RuntimeError]] `INFERRED`
- [[NATSMessageHandler]] `INFERRED`
- [[RateLimiter]] `INFERRED`
- [[MessageQueue]] `INFERRED`
- [[RealTimeEventHandler]] `INFERRED`
- [[CombatCommandHandler]] `INFERRED`
- [[RoomSubscriptionManager]] `INFERRED`
- [[PlayerRespawnEventHandler]] `INFERRED`
- [[FollowService]] `INFERRED`
- [[PartyService]] `INFERRED`
- [[Any]] `INFERRED`
- [[CombatCommandHandlerExtras]] `INFERRED`
- [[EventHandler]] `INFERRED`
- [[ConnectionMetadata]] `INFERRED`
- [[PlayerStateEventHandler]] `INFERRED`
- [[UUID]] `INFERRED`
- [[UUID]] `INFERRED`
- [[MemoryMonitor]] `INFERRED`
- [[Any]] `INFERRED`
- [[RealtimeBundle]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
