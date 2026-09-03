# Nats Retry Handler

> 11 nodes

## Key Concepts

- **.retry_async()** (5 connections) — `server/realtime/nats_retry_handler.py`
- **.calculate_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **.get_retry_stats()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **.retry_with_backoff()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **.update_config()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **Any** (3 connections)
- **Calculate exponential backoff delay with jitter. Args: attempt: Current attempt…** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Retry a function with exponential backoff. Args: func: Async function to retry…** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Get retry statistics. Returns: Dictionary with retry metrics AI: For monitoring…** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Retry async function with exponential backoff. Attempts the function up to…** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Update retry configuration dynamically. Allows runtime adjustment of retry…** (1 connections) — `server/realtime/nats_retry_handler.py`

## Relationships

- [Test Nats Retry Handler](Test_Nats_Retry_Handler.md) (6 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*