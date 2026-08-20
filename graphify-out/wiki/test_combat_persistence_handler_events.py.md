# test_combat_persistence_handler_events.py

> 95 nodes

## Key Concepts

- **test_combat_persistence_handler_events.py** (26 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **asyncio** (18 connections)
- **combat_persistence_handler.py** (16 connections) — `server/services/combat_persistence_handler.py`
- **test_combat_persistence_handler.py** (15 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **persistence_handler()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_event_bus_publish_error()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **persistence_handler()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_all_parameters()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_all_parameters_new()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_no_event_bus()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_outer_exception()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- *... and 70 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (4 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (4 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 148 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*