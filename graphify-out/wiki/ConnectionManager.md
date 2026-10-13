# ConnectionManager

> God node · 224 connections · `server/realtime/connection_manager.py`

**Community:** [Community 106](Community_106.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`

### contains
- connection_manager.py `EXTRACTED`

### imports
- server/dependencies.py `EXTRACTED`
- test_message_category_invariants.py `EXTRACTED`
- websocket_handler.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- event_handler.py `EXTRACTED`
- player_event_handlers.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- test_envelope.py `EXTRACTED`
- bundles/game.py `EXTRACTED`
- player_event_handlers_state.py `EXTRACTED`
- websocket_room_updates.py `EXTRACTED`
- test_room_system_message_categories.py `EXTRACTED`
- nats_message_handler.py `EXTRACTED`
- lifespan_protocols.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`

### method
- .event_bus() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._track_player_disconnected() `EXTRACTED`
- .handle_new_game_session() `EXTRACTED`
- .check_connection_health() `EXTRACTED`
- ._get_player() `EXTRACTED`
- .track_player_connected() `EXTRACTED`
- .broadcast_connection_message() `EXTRACTED`
- ._is_websocket_open() `EXTRACTED`
- ._safe_close_websocket() `EXTRACTED`
- .connect_websocket() `EXTRACTED`
- .disconnect_websocket() `EXTRACTED`
- .mark_player_seen() `EXTRACTED`
- .send_personal_message_old() `EXTRACTED`
- ._cleanup_dead_websocket() `EXTRACTED`
- ._validate_token() `EXTRACTED`
- ._get_players_batch() `EXTRACTED`
- .handle_new_login() `EXTRACTED`
- ._check_and_process_disconnect() `EXTRACTED`
- ._send_initial_game_state() `EXTRACTED`

### rationale_for
- Manages real-time connections for the game. This refactored version uses… `EXTRACTED`

### references
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- close_container() `EXTRACTED`
- emit_loot_all_event() `EXTRACTED`
- emit_container_opened_events() `EXTRACTED`
- emit_transfer_event() `EXTRACTED`
- emit_close_container_event() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- resolve_connection_manager() `EXTRACTED`
- .__init__() `EXTRACTED`
- .test_emit_loot_all_event_emission_error() `EXTRACTED`
- .test_emit_transfer_event_emission_error() `EXTRACTED`
- .test_emit_transfer_event_passes_updated_container() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._init_messaging_handlers_and_publisher() `EXTRACTED`
- .test_emit_loot_all_event_all_items_removed() `EXTRACTED`
- .test_emit_loot_all_event_calculates_items_removed() `EXTRACTED`
- .test_emit_loot_all_event_success() `EXTRACTED`
- .test_emit_loot_all_event_zero_items_removed() `EXTRACTED`

### uses
- FollowService `INFERRED`
- RoomSubscriptionManager `INFERRED`
- MessageQueue `INFERRED`
- CombatCommandHandler `INFERRED`
- PartyService `INFERRED`
- EventHandler `INFERRED`
- PlayerEventHandler `INFERRED`
- RealtimeBundle `INFERRED`
- build_room_update_event() `INFERRED`
- _FollowMovementHost `INFERRED`
- PlayerEventHandlerBase `INFERRED`
- _dispatch_player_dp_updated_payload() `INFERRED`
- TestEmitLootAllEvent `INFERRED`
- TestEmitCloseContainerEvent `INFERRED`
- TestEmitTransferEvent `INFERRED`
- _cleanup() `INFERRED`
- _send_combat_participant_updates() `INFERRED`
- _RespawnRoomHost `INFERRED`
- send_personalized_room_events() `INFERRED`
- TestEmitContainerOpenedEvents `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*