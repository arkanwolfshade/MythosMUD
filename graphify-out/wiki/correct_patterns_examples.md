# correct patterns examples

> 37 nodes

## Key Concepts

- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **.cleanup_combat_tracking()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **cleanup_handler()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats_no_end_combat_method()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats_no_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.cleanup_stale_combats()** (2 connections) — `server/services/combat_cleanup_handler.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_handler_init()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_combat_tracking()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_error()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_no_connection_manager()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_no_room_subscriptions()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **Any** (1 connections)
- **Handles combat cleanup and tracking operations.** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Initialize the cleanup handler.          Args:             combat_service: Refer** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Remove combat from tracking dictionaries.** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Clean up combats that have been inactive for too long.          Args:** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Initialize the combat service.** (1 connections) — `server/services/combat_service.py`
- **Unit tests for combat cleanup handler.  Tests the CombatCleanupHandler class for** (1 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- *... and 12 more nodes in this community*

## Relationships

- [command factories exploration](command_factories_exploration.md) (6 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (4 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [message nats handler](message_nats_handler.md) (2 shared connections)
- [game chat service](game_chat_service.md) (2 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (2 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [persistence container extended](persistence_container_extended.md) (1 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (1 shared connections)
- [combat validator validators](combat_validator_validators.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`

## Audit Trail

- EXTRACTED: 94 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*