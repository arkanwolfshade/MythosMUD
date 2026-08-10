# Inventory Command Models

> 97 nodes

## Key Concepts

- **NATSService** (72 connections) — `server/services/nats_service.py`
- **Any** (17 connections)
- **.disconnect()** (11 connections) — `server/services/nats_service.py`
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- **.connect()** (8 connections) — `server/services/nats_service.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **._flush_batch()** (7 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **.publish()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._get_connection()** (5 connections) — `server/services/nats_service.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service.py`
- **._close_all_subscriptions()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- **.unsubscribe()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._handle_disconnect_async()** (4 connections) — `server/services/nats_service.py`
- *... and 72 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (15 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (11 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (1 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 329 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*