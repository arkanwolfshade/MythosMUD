# Persistence Layer Refactoring Summary

> 34 nodes

## Key Concepts

- **test_combat_persistence_handler_events.py** (26 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **asyncio** (18 connections)
- **test_publish_player_dp_update_event_impl_event_bus_publish_error()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_all_parameters()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_all_parameters_new()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_no_event_bus()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_outer_exception()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_publish_error_new()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_success_new()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_all_parameters()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_legacy_subject()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_nats_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_no_event_bus()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_no_nats()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_with_nats()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **Test _publish_player_dp_correction_event handles errors gracefully.** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **Test _publish_player_dp_correction_event publishes correction event.** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **Test _publish_player_dp_update_event_impl handles no event bus.** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **Test _publish_player_dp_update_event_impl handles errors gracefully.** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **Unit tests for combat persistence handler - event publishing. Tests DP update…** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_connection_disconnection.py](test_connection_disconnection.py.md) (2 shared connections)
- [_resolved_npm](_resolved_npm.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [SessionManager](SessionManager.md) (1 shared connections)
- [Vitest Best Practices](Vitest_Best_Practices.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 62 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*