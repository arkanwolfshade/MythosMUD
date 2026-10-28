# connection_initialization.py

> 112 nodes · cohesion 0.03

## Key Concepts

- **connection_manager.py** (137 connections) — `server/realtime/connection_manager.py`
- **connection_cleanup_methods.py** (19 connections) — `server/realtime/connection_cleanup_methods.py`
- **canonical_room_id_impl()** (16 connections) — `server/realtime/connection_room_utils.py`
- **test_connection_cleanup_methods.py** (16 connections) — `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- **test_connection_room_utils.py** (16 connections) — `server/tests/unit/realtime/test_connection_room_utils.py`
- **test_connection_error_methods.py** (14 connections) — `server/tests/unit/realtime/test_connection_error_methods.py`
- **delegate_error_handler()** (12 connections) — `server/realtime/connection_delegates.py`
- **connection_error_methods.py** (11 connections) — `server/realtime/connection_error_methods.py`
- **cleanup_dead_connections_impl()** (10 connections) — `server/realtime/connection_cleanup_methods.py`
- **detect_and_handle_error_state_impl()** (10 connections) — `server/realtime/connection_error_methods.py`
- **connection_room_utils.py** (10 connections) — `server/realtime/connection_room_utils.py`
- **check_and_cleanup_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **cleanup_orphaned_data_impl()** (9 connections) — `server/realtime/connection_cleanup_methods.py`
- **handle_authentication_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_security_violation_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **handle_websocket_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **recover_from_error_impl()** (9 connections) — `server/realtime/connection_error_methods.py`
- **cleanup_ghost_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **force_cleanup_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_stale_players_impl()** (8 connections) — `server/realtime/connection_cleanup_methods.py`
- **prune_player_from_all_rooms_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **reconcile_room_presence_impl()** (7 connections) — `server/realtime/connection_room_utils.py`
- **Any** (6 connections)
- **UUID** (6 connections)
- **asyncio** (6 connections)
- *... and 87 more nodes in this community*

## Relationships

- [PlayerEnteredRoom](PlayerEnteredRoom.md) (22 shared connections)
- [ChatService](ChatService.md) (22 shared connections)
- [Room](Room.md) (11 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (10 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (9 shared connections)
- [SpellEffects](SpellEffects.md) (7 shared connections)
- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (4 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (4 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (4 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (4 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_error_methods.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_room_utils.py`
- `server/tests/unit/realtime/test_connection_cleanup_methods.py`
- `server/tests/unit/realtime/test_connection_error_methods.py`
- `server/tests/unit/realtime/test_connection_room_utils.py`

## Audit Trail

- EXTRACTED: 362 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*