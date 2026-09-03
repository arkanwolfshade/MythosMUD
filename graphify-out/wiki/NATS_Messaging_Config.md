# NATS Messaging Config

> 270 nodes

## Key Concepts

- **NATSError** (66 connections) — `server/services/nats_exceptions.py`
- **test_nats_service.py** (63 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSPublishError** (41 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (38 connections) — `server/services/nats_exceptions.py`
- **nats_service.py** (34 connections) — `server/services/nats_service.py`
- **NATSConfig** (33 connections) — `server/config/models/nats.py`
- **NATSMetrics** (33 connections) — `server/services/nats_metrics.py`
- **NATSServicePoolMixin** (28 connections) — `server/services/nats_service_pool.py`
- **NATSSubscribeError** (23 connections) — `server/services/nats_exceptions.py`
- **asyncio** (23 connections)
- **nats_service_pool.py** (20 connections) — `server/services/nats_service_pool.py`
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (14 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSHealthCheckError** (13 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **nats_service_connect.py** (11 connections) — `server/services/nats_service_connect.py`
- **NatsConnectOptions** (9 connections) — `server/services/nats_service_connect.py`
- **.publish_with_pool()** (9 connections) — `server/services/nats_service_pool.py`
- **TestNATSConnectionError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **._flush_batch()** (8 connections) — `server/services/nats_service_pool.py`
- *... and 245 more nodes in this community*

## Relationships

- [NATS Service Client](NATS_Service_Client.md) (75 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (30 shared connections)
- [Combat Events](Combat_Events.md) (17 shared connections)
- [Test Nats Message Handler](Test_Nats_Message_Handler.md) (15 shared connections)
- [Test Nats Message Handler Subzone](Test_Nats_Message_Handler_Subzone.md) (8 shared connections)
- [Cors](Cors.md) (6 shared connections)
- [Test Combat Persistence Handler Events](Test_Combat_Persistence_Handler_Events.md) (6 shared connections)
- [Connection State Machine](Connection_State_Machine.md) (6 shared connections)
- [Test Manager](Test_Manager.md) (5 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (4 shared connections)
- [Test Nats Message Handler Chat](Test_Nats_Message_Handler_Chat.md) (4 shared connections)
- [Nats Message Handler Processing](Nats_Message_Handler_Processing.md) (3 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/services/nats_service_connect.py`
- `server/services/nats_service_pool.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 555 (85%)
- INFERRED: 100 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*