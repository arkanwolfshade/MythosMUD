# Server Realtime (82)

> 16 nodes

## Key Concepts

- **RuntimeError** (12 connections)
- **.initialize()** (5 connections) — `server/container/bundles/chat.py`
- **test_handle_nats_message_runtime_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_runtime_error_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_property_resolution_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_event_handler_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_broadcast_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _process_single_message raises exception when event handler fails.** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_validation_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_nats_error_returns_false()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_uuid_conversion_error()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _handle_nats_message handles RuntimeError and adds to DLQ.** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _subscribe_to_subject returns False on NATSError.** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **ApplicationContainer** (1 connections)
- **Initialize chat service.** (1 connections) — `server/container/bundles/chat.py`
- **Test connection_manager property handles resolution errors gracefully.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`

## Relationships

- [Server Realtime (11)](Server_Realtime_%2811%29.md) (9 shared connections)
- [Server App (2)](Server_App_%282%29.md) (1 shared connections)
- [Server Game (12)](Server_Game_%2812%29.md) (1 shared connections)
- [Scripts Ci (3)](Scripts_Ci_%283%29.md) (1 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)
- [Server Container](Server_Container.md) (1 shared connections)
- [Server Quest](Server_Quest.md) (1 shared connections)
- [Server Realtime (13)](Server_Realtime_%2813%29.md) (1 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 31 (65%)
- INFERRED: 17 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*