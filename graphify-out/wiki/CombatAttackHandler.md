# CombatAttackHandler

> 142 nodes · cohesion 0.03

## Key Concepts

- **NATSService** (157 connections) — `server/services/nats_service.py`
- **test_nats_service.py** (62 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_helpers.py** (59 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **asyncio** (26 connections)
- **asyncio** (23 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_nats_service_init_with_config()** (6 connections) — `server/tests/unit/services/test_nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_no_available_connections()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_connected()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_running()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **.get_connection_stats()** (4 connections) — `server/services/nats_service.py`
- **.publish()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- *... and 117 more nodes in this community*

## Relationships

- [TestRoomDataFixer](TestRoomDataFixer.md) (40 shared connections)
- [arkham_grid_spec.py](arkham_grid_spec.py.md) (18 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (18 shared connections)
- [useRoomEditModal.ts](useRoomEditModal.ts.md) (17 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (6 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (5 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (3 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (3 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (3 shared connections)
- [NPCPopulationController](NPCPopulationController.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [combat_assist.py](combat_assist.py.md) (2 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 303 (72%)
- INFERRED: 117 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*