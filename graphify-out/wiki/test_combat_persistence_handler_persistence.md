# test combat persistence handler persistence

> 87 nodes

## Key Concepts

- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **test_combat_persistence_handler_persistence.py** (21 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
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
- **persistence_handler()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **test_persist_player_dp_sync_get_stats_error()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **test_persist_player_dp_sync_get_stats_error_new()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler_persistence.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_persistence_handler_init()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_container()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_container_error()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_async_persistence()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- *... and 62 more nodes in this community*

## Relationships

- [Any](Any.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (6 shared connections)
- [test movement monitor](test_movement_monitor.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [test command parser](test_command_parser.md) (1 shared connections)
- [test combat persistence handler events](test_combat_persistence_handler_events.md) (1 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler_persistence.py`

## Audit Trail

- EXTRACTED: 221 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*