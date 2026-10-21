# get_username_from_user

> 186 nodes · cohesion 0.02

## Key Concepts

- **EventBus** (225 connections) — `server/events/event_bus.py`
- **BaseEvent** (99 connections) — `server/events/event_types.py`
- **test_event_bus.py** (59 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (28 connections)
- **test_event_bus_lifecycle.py** (24 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **MockEventClass** (19 connections) — `server/tests/unit/events/test_event_bus.py`
- **asyncio** (11 connections)
- **_ExperienceEventBus** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **test_handle_event_async_async_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_sync_subscriber_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_no_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_task_result_async_with_error()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_inject_queue_full_and_invalid()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_queue_depth_grows_when_consumer_blocked()** (6 connections) — `server/tests/unit/events/test_event_bus.py`
- **.unsubscribe()** (5 connections) — `server/events/event_bus.py`
- **test_shutdown_finally_cancels_leftover_processing_task()** (5 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_shutdown_swallows_unexpected_exception()** (5 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_async_subscriber_error_isolation()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_inject_dispatches_to_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_multiple_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_publish_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_handle_event_async_no_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_service_shutdown_removes_subscribers()** (5 connections) — `server/tests/unit/events/test_event_bus.py`
- *... and 161 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (36 shared connections)
- [RoomLoader](RoomLoader.md) (27 shared connections)
- [combat_assist.py](combat_assist.py.md) (20 shared connections)
- [CombatInstance](CombatInstance.md) (19 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (14 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (11 shared connections)
- [Room](Room.md) (7 shared connections)
- [test_experience_procedures.py](test_experience_procedures.py.md) (6 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (6 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (5 shared connections)
- [SpellLearningService](SpellLearningService.md) (5 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/persistence/repositories/experience_repository.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/events/test_event_bus_lifecycle.py`

## Audit Trail

- EXTRACTED: 433 (77%)
- INFERRED: 130 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*