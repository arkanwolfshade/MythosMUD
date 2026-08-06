# combat validator validators

> 104 nodes

## Key Concepts

- **NATSService** (120 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (54 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (26 connections) — `server/config/models/nats.py`
- **nats_service.py** (24 connections) — `server/services/nats_service.py`
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **.disconnect()** (11 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **._close_all_subscriptions()** (4 connections) — `server/services/nats_service.py`
- **.unsubscribe()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._handle_disconnect_async()** (4 connections) — `server/services/nats_service.py`
- **test_nats_service_init_with_dict()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_none()** (4 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_create_tracked_task_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_on_error_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.validate_tls_files()** (3 connections) — `server/config/models/nats.py`
- **._drain_subscriptions()** (3 connections) — `server/services/nats_service.py`
- **._close_nats_connection()** (3 connections) — `server/services/nats_service.py`
- **._cancel_background_tasks()** (3 connections) — `server/services/nats_service.py`
- **._stop_health_monitoring()** (3 connections) — `server/services/nats_service.py`
- **.get_active_subscriptions()** (3 connections) — `server/services/nats_service.py`
- **._cleanup_connection_pool()** (3 connections) — `server/services/nats_service.py`
- **test_unsubscribe_from_subject_not_found()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_missing_subject_raises()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_build_connect_options_with_token()** (3 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- *... and 79 more nodes in this community*

## Relationships

- [player event state](player_event_state.md) (35 shared connections)
- [combat commands handler](combat_commands_handler.md) (17 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (10 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (5 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (5 shared connections)
- [game chat service](game_chat_service.md) (4 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (3 shared connections)
- [skill game service](skill_game_service.md) (3 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [holiday service services](holiday_service_services.md) (2 shared connections)
- [nats message handler](nats_message_handler.md) (2 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 429 (96%)
- INFERRED: 18 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*