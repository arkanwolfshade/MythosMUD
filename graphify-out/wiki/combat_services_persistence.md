# combat services persistence

> 69 nodes

## Key Concepts

- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **Any** (3 connections)
- **persistence_handler()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_event_bus_publish_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_no_event_bus()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_error()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_with_nats()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_legacy_subject()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_nats_error()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_no_nats()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- *... and 44 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (14 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [persistence combat handler](persistence_combat_handler.md) (3 shared connections)
- [persistence combat services](persistence_combat_services.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [services combat sync](services_combat_sync.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 187 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*