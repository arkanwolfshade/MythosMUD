# combat validator validators

> 84 nodes

## Key Concepts

- **NATSService** (120 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (54 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **.disconnect()** (11 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **._close_all_subscriptions()** (4 connections) — `server/services/nats_service.py`
- **.unsubscribe()** (4 connections) — `server/services/nats_service.py`
- **test_create_tracked_task_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_error_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **._drain_subscriptions()** (3 connections) — `server/services/nats_service.py`
- **._close_nats_connection()** (3 connections) — `server/services/nats_service.py`
- **._cancel_background_tasks()** (3 connections) — `server/services/nats_service.py`
- **._stop_health_monitoring()** (3 connections) — `server/services/nats_service.py`
- **.get_active_subscriptions()** (3 connections) — `server/services/nats_service.py`
- **._cleanup_connection_pool()** (3 connections) — `server/services/nats_service.py`
- **test_unsubscribe_from_subject_not_found()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_missing_subject_raises()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_build_connect_options_with_token()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_build_connect_options_with_user_password()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_subscribe_message_handler_bad_json_with_manual_ack()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.is_connected()** (2 connections) — `server/services/nats_service.py`
- **.get_subscription_count()** (2 connections) — `server/services/nats_service.py`
- **svc()** (2 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_check_connection_allowed_when_permitted()** (2 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_check_connection_blocked_by_state_machine()** (2 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- *... and 59 more nodes in this community*

## Relationships

- [target resolution service](target_resolution_service.md) (26 shared connections)
- [combat commands handler](combat_commands_handler.md) (10 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (9 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (6 shared connections)
- [commands communication say](commands_communication_say.md) (5 shared connections)
- [connection state machine](connection_state_machine.md) (3 shared connections)
- [commands inventory put](commands_inventory_put.md) (2 shared connections)
- [nats message handler](nats_message_handler.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (2 shared connections)
- [game chat service](game_chat_service.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 350 (96%)
- INFERRED: 13 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*