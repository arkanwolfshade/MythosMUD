# Vitest Best Practices

> 27 nodes

## Key Concepts

- **combat_persistence_handler.py** (16 connections) — `server/services/combat_persistence_handler.py`
- **test_combat_persistence_handler.py** (15 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **persistence_handler()** (4 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **fixture** (3 connections)
- **mock_player()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_container_error()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_async_persistence()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_get_persistence_layer_no_container()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_log_death_state_changes_death_threshold()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_log_death_state_changes_mortally_wounded()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_persist_player_dp_background_public_api()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **test_persistence_handler_init()** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _get_persistence_layer handles container errors.** (2 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Combat persistence handling logic. Handles player DP persistence, verification,…** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: The game tick loop will also check for dead players, but this provides…** (1 connections) — `server/services/combat_persistence_handler.py`
- **# NOTE: DP update event is now published IMMEDIATELY in process_attack()** (1 connections) — `server/services/combat_persistence_handler.py`
- **Unit tests for combat persistence handler - core functionality. Tests…** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Create mock combat service.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Create CombatPersistenceHandler instance.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test CombatPersistenceHandler initialization.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _get_persistence_layer gets persistence from container.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _get_persistence_layer returns None when container unavailable.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- **Test _log_death_state_changes logs death threshold.** (1 connections) — `server/tests/unit/services/test_combat_persistence_handler.py`
- *... and 2 more nodes in this community*

## Relationships

- [SessionManager](SessionManager.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (1 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)
- [Persistence Layer Refactoring Summary](Persistence_Layer_Refactoring_Summary.md) (1 shared connections)
- [test_security_utils.py](test_security_utils.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/services/combat_persistence_handler.py`
- `server/tests/unit/services/test_combat_persistence_handler.py`

## Audit Trail

- EXTRACTED: 43 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*