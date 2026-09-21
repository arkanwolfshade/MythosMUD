# test_combat_cleanup_handler.py

> 41 nodes

## Key Concepts

- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **cleanup_handler()** (4 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.cleanup_combat_tracking()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats_no_end_combat_method()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats_no_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **asyncio** (3 connections)
- **fixture** (3 connections)
- **.cleanup_stale_combats()** (2 connections) — `server/services/combat_cleanup_handler.py`
- **test_check_connection_state()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_error()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_no_connection_manager()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_no_room_subscriptions()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_combat_tracking()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_handler_init()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **Any** (1 connections)
- **Combat cleanup and management logic. Handles combat cleanup, tracking, and end-…** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Handles combat cleanup and tracking operations.** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Initialize the cleanup handler. Args: combat_service: Reference to the parent…** (1 connections) — `server/services/combat_cleanup_handler.py`
- *... and 16 more nodes in this community*

## Relationships

- [combat_service.py](combat_service.py.md) (4 shared connections)
- [get_config](get_config.md) (4 shared connections)
- [NATSError](NATSError.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (1 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (1 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`

## Audit Trail

- EXTRACTED: 71 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*