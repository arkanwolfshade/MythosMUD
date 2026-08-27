# verify_npc_occupants.py

> 14 nodes

## Key Concepts

- **NATSMessageHandler** (20 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (3 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **Start the NATS message handler and subscribe to subjects. Args:…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Stop the NATS message handler and unsubscribe from subjects. Returns: True if…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to all chat-related NATS subjects using NATSSubjectManager patterns.…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to chat subjects using NATSSubjectManager patterns. This method…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to a specific NATS subject. Args: subject: Subject string to…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Unsubscribe from a specific NATS subject. Returns: True if unsubscribed…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Handler for processing NATS messages and broadcasting to WebSocket clients.…** (1 connections) — `server/realtime/nats_message_handler.py`

## Relationships

- [InventoryCommandFactory](InventoryCommandFactory.md) (2 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [test_lint_raw_sql_in_python.py](test_lint_raw_sql_in_python.py.md) (1 shared connections)
- [Argon2 Password Hashing Best Practices](Argon2_Password_Hashing_Best_Practices.md) (1 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (1 shared connections)
- [login_grace_period.py](login_grace_period.py.md) (1 shared connections)
- [test_command_service.py](test_command_service.py.md) (1 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)
- [gameStore.ts](gameStore.ts.md) (1 shared connections)
- [test_admin_summon_command.py](test_admin_summon_command.py.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 24 (80%)
- INFERRED: 6 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*