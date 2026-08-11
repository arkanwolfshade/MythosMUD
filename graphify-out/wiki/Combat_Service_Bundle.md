# Combat Service Bundle

> 86 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_connection_pool()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_message_batch()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_not_initialized()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_no_available_connections()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_not_running()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_not_found()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_not_connected()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_timeout()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_error()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_state_machine_blocked()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_failure()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_connect_circuit_breaker_opens()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_flushes_batch()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_disconnect_handles_drain_error()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_publish_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_subscribe_with_manual_ack()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_unsubscribe_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_request_success()** (2 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [Inventory Command Models](Inventory_Command_Models.md) (19 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (17 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (4 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (2 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 207 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*