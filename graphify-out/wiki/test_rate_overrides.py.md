# test_rate_overrides.py

> 54 nodes · cohesion 0.06

## Key Concepts

- **NATSSubscribeError** (23 connections) — `server/services/nats_exceptions.py`
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (13 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSConnectionError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **Exception** (6 connections)
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_all_errors_inherit_from_nats_error()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_with_original_error()** (4 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.__init__()** (3 connections) — `server/services/nats_exceptions.py`
- **.test_exception_can_be_caught_by_base()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_exception_can_be_raised()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_creation()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_with_all_parameters()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_connection_error_with_url()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_health_check_error_creation()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_health_check_error_default_consecutive_failures()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.test_health_check_error_with_consecutive_failures()** (3 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- *... and 29 more nodes in this community*

## Relationships

- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (10 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (8 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (5 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (4 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (3 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 102 (86%)
- INFERRED: 17 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*