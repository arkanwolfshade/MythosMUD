# player event state

> 64 nodes

## Key Concepts

- **Any** (17 connections)
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- **.connect()** (8 connections) — `server/services/nats_service.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **._flush_batch()** (7 connections) — `server/services/nats_service.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **.publish()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._get_connection()** (5 connections) — `server/services/nats_service.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._on_reconnect()** (4 connections) — `server/services/nats_service.py`
- **NATS** (4 connections)
- **._return_connection()** (4 connections) — `server/services/nats_service.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service.py`
- **._check_connection_allowed()** (3 connections) — `server/services/nats_service.py`
- **._setup_connection_handlers()** (3 connections) — `server/services/nats_service.py`
- **._perform_health_check()** (3 connections) — `server/services/nats_service.py`
- **._decode_message_data()** (3 connections) — `server/services/nats_service.py`
- *... and 39 more nodes in this community*

## Relationships

- [combat validator validators](combat_validator_validators.md) (35 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [connection state machine](connection_state_machine.md) (1 shared connections)
- [combat commands handler](combat_commands_handler.md) (1 shared connections)
- [manager subject services](manager_subject_services.md) (1 shared connections)
- [skill game service](skill_game_service.md) (1 shared connections)
- [game chat service](game_chat_service.md) (1 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 190 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*