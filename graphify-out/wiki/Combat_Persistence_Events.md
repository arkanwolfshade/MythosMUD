# Combat Persistence Events

> 111 nodes

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
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service.py`
- **._close_all_subscriptions()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- **.unsubscribe()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- *... and 86 more nodes in this community*

## Relationships

- [Inventory Command Models](Inventory_Command_Models.md) (13 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (11 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (3 shared connections)
- [Player Death Service](Player_Death_Service.md) (3 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (2 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (2 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (2 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (2 shared connections)
- [NPC Spawn Validator](NPC_Spawn_Validator.md) (1 shared connections)
- [Health Check Models](Health_Check_Models.md) (1 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (1 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 358 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*