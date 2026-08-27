# NPCLifecycleManager

> 167 nodes

## Key Concepts

- **EventBus** (208 connections) — `server/events/event_bus.py`
- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **test_event_bus_lifecycle.py** (25 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (11 connections)
- **test_event_bus_inject_dispatches_to_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_async_subscriber_error()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_queue_depth_grows_when_consumer_blocked()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **.unsubscribe()** (4 connections) — `server/events/event_bus.py`
- **event_bus()** (4 connections) — `server/tests/unit/events/test_event_bus.py`
- **event_bus()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_abandon_pending_tasks_cancels_and_drains()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_active_tasks_best_effort_cancels_running_tasks()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_and_wait_for_active_tasks_abandons_pending()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_and_wait_for_active_tasks_all_already_done()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_processing_task_swallows_timeout()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- *... and 142 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (28 shared connections)
- [Invite](Invite.md) (27 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [_apply_arena_seed_patch.py](_apply_arena_seed_patch.py.md) (4 shared connections)
- [RoomLoader](RoomLoader.md) (4 shared connections)
- [MythosMUDError](MythosMUDError.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (3 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)
- [tailwind Best Practices](tailwind_Best_Practices.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_bus_lifecycle.py`

## Audit Trail

- EXTRACTED: 332 (78%)
- INFERRED: 92 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*