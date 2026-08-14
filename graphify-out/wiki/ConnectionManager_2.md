# ConnectionManager

> God node · 267 connections · `server/realtime/connection_manager.py`

**Community:** [ConnectionManager](ConnectionManager.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`

### contains
- [connection_manager.py](connection_manager.py.md) `EXTRACTED`

### imports
- [server/dependencies.py](server-dependencies.py.md) `EXTRACTED`
- [websocket_handler.py](websocket_handler.py.md) `EXTRACTED`
- [container_endpoints_basic.py](container_endpoints_basic.py.md) `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- combat_handler.py `EXTRACTED`
- [websocket_initial_state.py](websocket_initial_state.py.md) `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- event_handler.py `EXTRACTED`
- nats_message_handler.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- websocket_room_updates.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- test_envelope.py `EXTRACTED`
- [container_events.py](container_events.py.md) `EXTRACTED`
- combat_loader.py `EXTRACTED`
- websocket_handler_message_loop.py `EXTRACTED`
- api/game.py `EXTRACTED`
- follow_service.py `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- .event_bus() `EXTRACTED`
- .check_connection_health() `EXTRACTED`
- ._get_player() `EXTRACTED`
- ._track_player_disconnected() `EXTRACTED`
- .canonical_room_id() `EXTRACTED`
- .connect_websocket() `EXTRACTED`
- .disconnect_websocket() `EXTRACTED`
- ._get_players_batch() `EXTRACTED`
- ._track_player_connected() `EXTRACTED`
- ._broadcast_connection_message() `EXTRACTED`
- ._send_initial_game_state() `EXTRACTED`
- ._is_websocket_open() `EXTRACTED`
- ._safe_close_websocket() `EXTRACTED`
- .get_player_websocket_connection_id() `EXTRACTED`
- .has_websocket_connection() `EXTRACTED`
- .get_connection_count() `EXTRACTED`
- .subscribe_to_room() `EXTRACTED`
- .unsubscribe_from_room() `EXTRACTED`
- ._prune_player_from_all_rooms() `EXTRACTED`

### rationale_for
- Manages real-time connections for the game. This refactored version uses… `EXTRACTED`

### references
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- close_container() `EXTRACTED`
- emit_loot_all_event() `EXTRACTED`
- emit_transfer_event() `EXTRACTED`
- emit_container_opened_events() `EXTRACTED`
- emit_close_container_event() `EXTRACTED`
- safe_close_websocket_impl() `EXTRACTED`
- resolve_connection_manager() `EXTRACTED`
- force_disconnect_player_impl() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _dispatch_player_dp_updated_payload() `EXTRACTED`
- broadcast_to_room_impl() `EXTRACTED`
- get_player_impl() `EXTRACTED`
- get_players_batch_impl() `EXTRACTED`
- _send_combat_participant_updates() `EXTRACTED`
- .__init__() `EXTRACTED`
- broadcast_global_event_impl() `EXTRACTED`
- broadcast_global_impl() `EXTRACTED`

### uses
- [RateLimiter](RateLimiter.md) `INFERRED`
- [CombatCommandHandler](CombatCommandHandler.md) `INFERRED`
- [MessageQueue](MessageQueue.md) `INFERRED`
- [RoomSubscriptionManager](RoomSubscriptionManager.md) `INFERRED`
- [RealTimeEventHandler](RealTimeEventHandler.md) `INFERRED`
- FollowService `INFERRED`
- [PartyService](PartyService.md) `INFERRED`
- [EventHandler](EventHandler.md) `INFERRED`
- PlayerRespawnEventHandler `INFERRED`
- RealtimeBundle `INFERRED`
- [EventPublisher](EventPublisher.md) `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- NATSMessageHandler `INFERRED`
- ConnectionMetadata `INFERRED`
- _NpcWithLife `INFERRED`
- PlayerStateEventHandler `INFERRED`
- RespawnPlayerEventPayload `INFERRED`
- TestEmitLootAllEvent `INFERRED`
- TestEmitCloseContainerEvent `INFERRED`
- TestEmitTransferEvent `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*