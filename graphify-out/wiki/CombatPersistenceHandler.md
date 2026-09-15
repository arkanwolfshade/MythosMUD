# CombatPersistenceHandler

> 49 nodes

## Key Concepts

- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **test_combat_persistence_handler.py** (14 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **UUID** (8 connections)
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_sync()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **persistence_handler()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Any** (3 connections)
- **fixture** (3 connections)
- **mock_player()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_container_error()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_async_persistence()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_container()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_log_death_state_changes_death_threshold()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_log_death_state_changes_mortally_wounded()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_persist_player_dp_background_public_api()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- *... and 24 more nodes in this community*

## Relationships

- [test_combat_persistence_handler_events.py](test_combat_persistence_handler_events.py.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (3 shared connections)
- [test_combat_persistence_handler_persistence.py](test_combat_persistence_handler_persistence.py.md) (2 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [CombatTurnProcessor](CombatTurnProcessor.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 83 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*