# test_container_persistence_async_helpers.py

> 190 nodes · cohesion 0.02

## Key Concepts

- **time.py** (107 connections) — `server/container/bundles/time.py`
- **RateLimiter** (69 connections) — `server/realtime/rate_limiter.py`
- **RoomSubscriptionManager** (62 connections) — `server/realtime/room_subscription_manager.py`
- **connection_initialization.py** (39 connections) — `server/realtime/connection_initialization.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **PerformanceTracker** (28 connections) — `server/realtime/monitoring/performance_tracker.py`
- **statistics_aggregator.py** (26 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **room_subscription_manager.py** (23 connections) — `server/realtime/room_subscription_manager.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
- **health_monitor.py** (16 connections) — `server/realtime/monitoring/health_monitor.py`
- **performance_tracker.py** (14 connections) — `server/realtime/monitoring/performance_tracker.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **server/realtime/monitoring/__init__.py** (7 connections) — `server/realtime/monitoring/__init__.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._add_npc_to_occupants()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **mock_manager()** (6 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **._build_stats_response()** (5 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.get_stats()** (5 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.add_room_drop()** (5 connections) — `server/realtime/room_subscription_manager.py`
- *... and 165 more nodes in this community*

## Relationships

- [Room](Room.md) (21 shared connections)
- [SpellEffects](SpellEffects.md) (16 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (15 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (15 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (10 shared connections)
- [container_helpers_inventory_ops.py](container_helpers_inventory_ops.py.md) (10 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (9 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (9 shared connections)
- [ContainerService](ContainerService.md) (9 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (8 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (8 shared connections)
- [test_quest_service.py](test_quest_service.py.md) (8 shared connections)

## Source Files

- `server/container/bundles/time.py`
- `server/realtime/connection_initialization.py`
- `server/realtime/monitoring/__init__.py`
- `server/realtime/monitoring/health_monitor.py`
- `server/realtime/monitoring/performance_tracker.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`

## Audit Trail

- EXTRACTED: 524 (93%)
- INFERRED: 37 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*