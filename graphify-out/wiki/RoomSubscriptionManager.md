# RoomSubscriptionManager

> 142 nodes

## Key Concepts

- **RoomSubscriptionManager** (50 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **RoomEventHandler** (21 connections) — `server/realtime/integration/room_event_handler.py`
- **room_subscription_manager.py** (20 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_room_event_handler.py** (14 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_room_subscription_manager_npcs.py** (14 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **room_event_handler.py** (13 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (13 connections)
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **asyncio** (9 connections)
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (8 connections)
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **._add_npc_to_occupants()** (5 connections) — `server/realtime/room_subscription_manager.py`
- *... and 117 more nodes in this community*

## Relationships

- [RateLimiter](RateLimiter.md) (12 shared connections)
- [connection_manager.py](connection_manager.py.md) (11 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (9 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (6 shared connections)
- [GameStateProvider](GameStateProvider.md) (4 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (4 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [test_room_subscription_manager.py](test_room_subscription_manager.py.md) (3 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (3 shared connections)
- [test_room_subscription_manager_helpers.py](test_room_subscription_manager_helpers.py.md) (3 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/integration/test_room_event_handler.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 303 (92%)
- INFERRED: 26 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*