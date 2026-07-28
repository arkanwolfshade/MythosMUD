# Server Realtime (104)

> 10 nodes

## Key Concepts

- **send_personal_message_old_impl()** (13 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_queue_message_if_needed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl_no_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Queue message for later delivery if no active connections.      Args:         pl** (1 connections) — `server/realtime/connection_helpers.py`
- **Send a personal message to a player via WebSocket (deprecated implementation).** (1 connections) — `server/realtime/connection_helpers.py`
- **Test _queue_message_if_needed() queues message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test send_personal_message_old_impl() sends message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test send_personal_message_old_impl() when no connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [Server Realtime (77)](Server_Realtime_%2877%29.md) (6 shared connections)
- [Server Realtime (98)](Server_Realtime_%2898%29.md) (3 shared connections)
- [Server Realtime (93)](Server_Realtime_%2893%29.md) (2 shared connections)
- [Server Persistence](Server_Persistence.md) (1 shared connections)
- [Server Realtime (112)](Server_Realtime_%28112%29.md) (1 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*