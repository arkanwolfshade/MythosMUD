# EventBus

> 195 nodes

## Key Concepts

- **EventBus** (207 connections) — `server/events/event_bus.py`
- **BaseEvent** (93 connections) — `server/events/event_types.py`
- **test_event_bus.py** (60 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **UUID** (9 connections)
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **._stop_processing()** (7 connections) — `server/events/event_bus.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_queue_depth_grows_when_consumer_blocked()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **Any** (6 connections)
- **._abandon_pending_tasks()** (5 connections) — `server/events/event_bus.py`
- **._cancel_and_wait_for_active_tasks()** (5 connections) — `server/events/event_bus.py`
- **._cancel_task_quietly()** (5 connections) — `server/events/event_bus.py`
- **._create_async_subscriber_tasks()** (5 connections) — `server/events/event_bus.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_update_event()** (5 connections) — `server/services/combat_hp_sync.py`
- **test_async_subscriber_error_isolation()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 170 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (57 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (20 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [test_event_handler.py](test_event_handler.py.md) (15 shared connections)
- [DistributedEventBus](DistributedEventBus.md) (11 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (8 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (8 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (6 shared connections)
- [test_party_flow.py](test_party_flow.py.md) (5 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (5 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/npc/event_reaction_system.py`
- `server/services/combat_hp_sync.py`
- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 447 (82%)
- INFERRED: 101 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*