# room game service

> 2 nodes

## Key Concepts

- **test_process_message_with_retry_exhaustion()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **Test _process_message_with_retry adds to DLQ and re-raises when all retries exha** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`

## Relationships

- [nats message handler](nats_message_handler.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 3 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*