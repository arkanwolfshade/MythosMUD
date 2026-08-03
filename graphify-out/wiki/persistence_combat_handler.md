# persistence combat handler

> 27 nodes

## Key Concepts

- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **test_combat_persistence_handler.py** (14 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **persistence_handler()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_persistence_handler_init()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_container()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_container_error()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_async_persistence()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_log_death_state_changes_death_threshold()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_log_death_state_changes_mortally_wounded()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_persist_player_dp_background_public_api()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Combat persistence handling logic.  Handles player DP persistence, verification,** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: The game tick loop will also check for dead players, but this provides i** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: DP update event is now published IMMEDIATELY in process_attack()** (1 connections) — `server/services/combat_persistence_handler.py`
- **mock_player()** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Unit tests for combat persistence handler - core functionality.  Tests initializ** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Create mock combat service.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Create CombatPersistenceHandler instance.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test CombatPersistenceHandler initialization.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _get_persistence_layer gets persistence from container.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _get_persistence_layer returns None when container unavailable.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _get_persistence_layer handles container errors.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _get_persistence_layer handles container without async_persistence.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _log_death_state_changes logs death threshold.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- *... and 2 more nodes in this community*

## Relationships

- [spawn npc services](spawn_npc_services.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (1 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (1 shared connections)
- [commands communication say](commands_communication_say.md) (1 shared connections)
- [persistence combat services](persistence_combat_services.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 65 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*