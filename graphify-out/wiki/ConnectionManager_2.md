# ConnectionManager

> God node · 255 connections · `server/realtime/connection_manager.py`

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
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- player_event_handlers.py `EXTRACTED`
- event_handler.py `EXTRACTED`
- nats_message_handler.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- [websocket_handler_commands.py](websocket_handler_commands.py.md) `EXTRACTED`
- websocket_room_updates.py `EXTRACTED`
- api/game.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- [test_envelope.py](test_envelope.py.md) `EXTRACTED`
- websocket_handler_message_loop.py `EXTRACTED`
- [container_events.py](container_events.py.md) `EXTRACTED`
- [combat_loader.py](combat_loader.py.md) `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- .event_bus() `EXTRACTED`
- .check_connection_health() `EXTRACTED`
- ._get_player() `EXTRACTED`
- ._track_player_disconnected() `EXTRACTED`
- .canonical_room_id() `EXTRACTED`
- .connect_websocket() `EXTRACTED`
- .disconnect_websocket() `EXTRACTED`
- .handle_new_game_session() `EXTRACTED`
- ._get_players_batch() `EXTRACTED`
- .track_player_connected() `EXTRACTED`
- .broadcast_connection_message() `EXTRACTED`
- ._send_initial_game_state() `EXTRACTED`
- ._is_websocket_open() `EXTRACTED`
- ._safe_close_websocket() `EXTRACTED`
- .get_player_websocket_connection_id() `EXTRACTED`
- .has_websocket_connection() `EXTRACTED`
- .get_connection_count() `EXTRACTED`
- .subscribe_to_room() `EXTRACTED`
- .unsubscribe_from_room() `EXTRACTED`

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
- resolve_connection_manager() `EXTRACTED`
- force_disconnect_player_impl() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- broadcast_to_room_impl() `EXTRACTED`
- get_player_impl() `EXTRACTED`
- get_players_batch_impl() `EXTRACTED`
- .__init__() `EXTRACTED`
- broadcast_global_event_impl() `EXTRACTED`
- broadcast_global_impl() `EXTRACTED`
- broadcast_room_event_impl() `EXTRACTED`
- get_message_delivery_stats_impl() `EXTRACTED`

### uses
- [RateLimiter](RateLimiter.md) `INFERRED`
- MessageQueue `INFERRED`
- [CombatCommandHandler](CombatCommandHandler.md) `INFERRED`
- [RoomSubscriptionManager](RoomSubscriptionManager.md) `INFERRED`
- FollowService `INFERRED`
- [PartyService](PartyService.md) `INFERRED`
- RealtimeBundle `INFERRED`
- [EventHandler](EventHandler.md) `INFERRED`
- PlayerRespawnEventHandler `INFERRED`
- [EventPublisher](EventPublisher.md) `INFERRED`
- PlayerEventHandler `INFERRED`
- ConnectionMetadata `INFERRED`
- PlayerStateEventHandler `INFERRED`
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) `INFERRED`
- TestEmitTransferEvent `INFERRED`
- TestEmitCloseContainerEvent `INFERRED`
- _dispatch_player_dp_updated_payload() `INFERRED`
- _send_combat_participant_updates() `INFERRED`
- TestEmitContainerOpenedEvents `INFERRED`
- _npc_died_broadcast_and_bridge() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*