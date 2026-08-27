# security.ts

> 34 nodes

## Key Concepts

- **connection_delegates.py** (40 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **UUID** (10 connections)
- **delegate_personal_message_sender_sync()** (9 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (9 connections) — `server/realtime/connection_delegates.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (8 connections) — `server/realtime/connection_delegates.py`
- **_WebsocketCleanupManager** (7 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **_remove_connection_from_player_list()** (5 connections) — `server/realtime/connection_delegates.py`
- **_sync_callable()** (5 connections) — `server/realtime/connection_delegates.py`
- **WebSocket** (5 connections)
- **_websocket_client_connected()** (4 connections) — `server/realtime/connection_delegates.py`
- **convert_room_players_uuids_to_names_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **handle_player_left_room_impl()** (4 connections) — `server/realtime/connection_manager_methods.py`
- **_is_benign_websocket_close_error()** (3 connections) — `server/realtime/connection_delegates.py`
- **Delegation helpers for connection manager. This module provides helper…** (1 connections) — `server/realtime/connection_delegates.py`
- **Drop connection_id from player_websockets; delete empty player entries.** (1 connections) — `server/realtime/connection_delegates.py`
- **Generic delegate for health monitor methods.** (1 connections) — `server/realtime/connection_delegates.py`
- **Generic delegate for synchronous health monitor methods.** (1 connections) — `server/realtime/connection_delegates.py`
- **Generic delegate for game state provider methods. Args: game_state_provider:…** (1 connections) — `server/realtime/connection_delegates.py`
- **Generic delegate for synchronous game state provider methods. Args:…** (1 connections) — `server/realtime/connection_delegates.py`
- *... and 9 more nodes in this community*

## Relationships

- [submitAuth.ts](submitAuth.ts.md) (33 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (16 shared connections)
- [test_message_handler_factory.py](test_message_handler_factory.py.md) (9 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (5 shared connections)
- [🚫 Anti-Patterns NOT Found (Good!)](🚫_Anti-Patterns_NOT_Found_Good!.md) (4 shared connections)
- [test_chat_logger.py](test_chat_logger.py.md) (4 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (3 shared connections)
- [P3 · realtime-connection + events-nats](P3_·_realtime-connection_+_events-nats.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 132 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*