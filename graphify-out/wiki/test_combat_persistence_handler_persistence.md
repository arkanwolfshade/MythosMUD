# test combat persistence handler persistence

> 92 nodes

## Key Concepts

- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **test_combat_persistence_handler.py** (14 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
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
- **persistence_handler()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **persistence_handler()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_event_bus_publish_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_persistence_handler_init()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_container()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_container_error()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_async_persistence()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_log_death_state_changes_death_threshold()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- *... and 67 more nodes in this community*

## Relationships

- [Any](Any.md) (10 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (4 shared connections)
- [Test get room environment() treats](Test_get_room_environment%28%29_treats.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [close db()](close_db%28%29.md) (2 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 234 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*