# event bus events

> 23 nodes

## Key Concepts

- **test_event_bus.py** (57 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_init()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_get_all_subscriber_counts_empty()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_shutdown_idempotent()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_invalid_event_type()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_publish_invalid_event()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_processing_started()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_multiple_services_subscribe_same_events_integration()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_and_lifecycle_metrics()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_set_main_loop_and_ensure_processing()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_signal_shutdown_and_cancel_helpers()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_active_task_details_includes_exception()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_ensure_async_processing_no_loop_logs()** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Unit tests for event bus.  Tests the EventBus class.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus initialization.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() stops processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_all_subscriber_counts() with no subscribers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.shutdown() is idempotent.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test unsubscribe() raises error for invalid event type.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test publish() raises error for invalid event.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test _ensure_processing_started() calls _ensure_async_processing.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Integration test: Multiple services subscribing to same events and cleanup.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [services exploration service](services_exploration_service.md) (11 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [realtime player event](realtime_player_event.md) (3 shared connections)
- [game room service](game_room_service.md) (2 shared connections)
- [room toolkit validator](room_toolkit_validator.md) (2 shared connections)
- [item models rationale](item_models_rationale.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (1 shared connections)
- [services chat rate](services_chat_rate.md) (1 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (1 shared connections)
- [infrastructure security rationale](infrastructure_security_rationale.md) (1 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 87 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*