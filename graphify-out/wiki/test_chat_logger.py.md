# test_chat_logger.py

> 31 nodes

## Key Concepts

- **asyncio** (17 connections)
- **broadcast_to_room_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_global_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_manager_methods.py`
- **check_all_connections_health_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **get_room_occupants_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **handle_player_entered_room_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **periodic_health_check_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **subscribe_to_room_events_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **unsubscribe_from_room_events_impl()** (5 connections) — `server/realtime/connection_manager_methods.py`
- **test_broadcast_global_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_global_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_room_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_broadcast_to_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_check_all_connections_health_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_get_room_occupants_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_handle_player_entered_room_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_periodic_health_check_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_subscribe_to_room_events_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_unsubscribe_from_room_events_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **Broadcast a message to all players in a room.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Broadcast a message to all connected players.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_manager_methods.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_manager_methods.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_message_handler_factory.py](test_message_handler_factory.py.md) (27 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (10 shared connections)
- [security.ts](security.ts.md) (4 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [submitAuth.ts](submitAuth.ts.md) (2 shared connections)
- [.create_equip_command](create_equip_command.md) (2 shared connections)
- [_parse_env_list](_parse_env_list.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 80 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*