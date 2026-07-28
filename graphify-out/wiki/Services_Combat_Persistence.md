# Services Combat Persistence

> 69 nodes · cohesion 0.04

## Key Concepts

- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_persistence_handler.py`
- **._get_persistence_layer()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_update_event_impl()** (6 connections) — `server/services/combat_persistence_handler.py`
- **._publish_player_dp_correction_event()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._verify_player_save()** (5 connections) — `server/services/combat_persistence_handler.py`
- **._log_death_state_changes()** (4 connections) — `server/services/combat_persistence_handler.py`
- **._persist_player_dp_background()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.publish_player_dp_update_event()** (4 connections) — `server/services/combat_persistence_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_persistence_handler.py`
- **Any** (3 connections)
- **persistence_handler()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_update_event_impl_event_bus_publish_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_all_parameters()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_all_parameters_new()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_error()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_no_event_bus()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_outer_exception()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_publish_error_new()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **test_publish_player_dp_correction_event_success_new()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- *... and 44 more nodes in this community*

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (6 shared connections)
- [E2E Session Report](E2E_Session_Report.md) (3 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (3 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (2 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`

## Audit Trail

- EXTRACTED: 187 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*