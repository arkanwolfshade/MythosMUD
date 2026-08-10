# Error Handling Guide

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

- [Combat Domain Events](Combat_Domain_Events.md) (13 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [AI Development Workflow](AI_Development_Workflow_2.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (1 shared connections)

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