# test_combat_persistence_handler_events.py

> 48 nodes

## Key Concepts

- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **asyncio** (18 connections)
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **persistence_handler()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_event_bus_publish_error()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
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
- **fixture** (2 connections)
- **Combat persistence handling logic. Handles player DP persistence, verification,…** (1 connections) — `server/services/combat_persistence_handler.py`
- *... and 23 more nodes in this community*

## Relationships

- [CombatPersistenceHandler](CombatPersistenceHandler.md) (5 shared connections)
- [NATSError](NATSError.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [test_combat_persistence_handler_persistence.py](test_combat_persistence_handler_persistence.py.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 79 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*