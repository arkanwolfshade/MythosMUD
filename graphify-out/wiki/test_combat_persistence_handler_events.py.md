# test_combat_persistence_handler_events.py

> 99 nodes

## Key Concepts

- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **CombatPersistenceHandler** (24 connections) — `server/services/combat_persistence_handler.py`
- **asyncio** (18 connections)
- **combat_persistence_handler.py** (16 connections) — `server/services/combat_persistence_handler.py`
- **test_combat_persistence_handler.py** (14 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **UUID** (9 connections)
- **._publish_player_dp_update_event_impl()** (7 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_sync()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_dp_event_to_bus()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **persistence_handler()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_event_bus_publish_error()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **persistence_handler()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **._publish_dp_update_to_nats()** (3 connections) — `server/services/combat_persistence_handler.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_all_parameters()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_all_parameters_new()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- *... and 74 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (6 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (4 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 154 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*