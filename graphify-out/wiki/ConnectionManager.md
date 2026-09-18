# ConnectionManager

> God node · 173 connections · `server/realtime/connection_manager.py`

**Community:** [Community 92](Community_92.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`

### contains
- connection_manager.py `EXTRACTED`

### imports
- server/dependencies.py `EXTRACTED`
- websocket_handler.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- player_event_handlers.py `EXTRACTED`
- nats_message_handler.py `EXTRACTED`
- websocket_handler_commands.py `EXTRACTED`
- player_event_handlers_state.py `EXTRACTED`
- lifespan_protocols.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- websocket_room_updates.py `EXTRACTED`
- follow_movement.py `EXTRACTED`
- websocket_handler_message_loop.py `EXTRACTED`
- api/game.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- test_envelope.py `EXTRACTED`

### method
- .event_bus() `EXTRACTED`
- ._track_player_disconnected() `EXTRACTED`
- .disconnect_websocket() `EXTRACTED`
- ._get_player() `EXTRACTED`
- .track_player_connected() `EXTRACTED`
- .broadcast_connection_message() `EXTRACTED`
- .connect_websocket() `EXTRACTED`
- .force_disconnect_player() `EXTRACTED`
- .handle_new_game_session() `EXTRACTED`
- .check_connection_health() `EXTRACTED`
- ._get_players_batch() `EXTRACTED`
- ._check_and_process_disconnect() `EXTRACTED`
- ._send_initial_game_state() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._is_websocket_open() `EXTRACTED`
- ._safe_close_websocket() `EXTRACTED`
- .get_player_websocket_connection_id() `EXTRACTED`
- .has_websocket_connection() `EXTRACTED`
- .get_connection_count() `EXTRACTED`
- .subscribe_to_room() `EXTRACTED`

### rationale_for
- Manages real-time connections for the game. This refactored version uses… `EXTRACTED`

### references
- resolve_connection_manager() `EXTRACTED`

### uses
- FollowService `INFERRED`
- PlayerRespawnEventHandler `INFERRED`
- CombatCommandHandler `INFERRED`
- PlayerStateEventHandler `INFERRED`
- PartyService `INFERRED`
- EventHandler `INFERRED`
- PlayerEventHandler `INFERRED`
- RealtimeBundle `INFERRED`
- _FollowMovementHost `INFERRED`
- build_room_update_event() `INFERRED`
- _dispatch_player_dp_updated_payload() `INFERRED`
- TestEmitLootAllEvent `INFERRED`
- TestEmitTransferEvent `INFERRED`
- TestEmitCloseContainerEvent `INFERRED`
- _send_combat_participant_updates() `INFERRED`
- send_personalized_room_events() `INFERRED`
- _RespawnRoomHost `INFERRED`
- _dispatch_player_dp_decay_payload() `INFERRED`
- TestEmitContainerOpenedEvents `INFERRED`
- _npc_died_broadcast_and_bridge() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*