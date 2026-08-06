# command player state

> 131 nodes

## Key Concepts

- **RoomSubscriptionManager** (46 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **MemoryMonitor** (27 connections) — `server/realtime/memory_monitor.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **test_memory_monitor.py** (21 connections) — `server/tests/unit/realtime/test_memory_monitor.py`
- **room_subscription_manager.py** (18 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **memory_monitor.py** (10 connections) — `server/realtime/memory_monitor.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **Any** (8 connections)
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **_max_connection_age_seconds()** (7 connections) — `server/realtime/memory_monitor.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- *... and 106 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (16 shared connections)
- [Room Broadcast](Room_Broadcast.md) (13 shared connections)
- [persistence rationale room](persistence_rationale_room.md) (11 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (9 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (6 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (6 shared connections)
- [combat configuration service](combat_configuration_service.md) (6 shared connections)
- [room subscription manager](room_subscription_manager.md) (6 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (4 shared connections)
- [spell models rationale](spell_models_rationale.md) (4 shared connections)
- [command utility models](command_utility_models.md) (4 shared connections)
- [tick game processing](tick_game_processing.md) (4 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_memory_monitor.py`

## Audit Trail

- EXTRACTED: 556 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*