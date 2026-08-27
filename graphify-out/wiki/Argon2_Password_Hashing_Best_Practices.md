# Argon2 Password Hashing Best Practices

> 28 nodes

## Key Concepts

- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **UUID** (3 connections)
- **TypedDict** (2 connections)
- **Process message with retry logic. Attempts message processing with exponential…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Process a single NATS message (original logic, can raise exceptions). Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Extract and normalize chat message fields from message data. Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Extracted chat fields before required-field validation.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Validate that all required chat message fields are present. Args: chat_fields:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Build a WebSocket chat event from chat fields and formatted message. Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Convert string IDs to UUIDs for broadcasting. Args: sender_id: Sender player ID…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Broadcast message based on channel type using strategy pattern. Args: channel:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Chat fields after required string fields are validated.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Narrow a message field to str | None.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 3 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (7 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (3 shared connections)
- [verify_npc_occupants.py](verify_npc_occupants.py.md) (1 shared connections)
- [🟢 MEDIUM PRIORITY IMPROVEMENTS](🟢_MEDIUM_PRIORITY_IMPROVEMENTS.md) (1 shared connections)
- [gameStore.ts](gameStore.ts.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [RateLimiter](RateLimiter.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_processing.py`

## Audit Trail

- EXTRACTED: 52 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*