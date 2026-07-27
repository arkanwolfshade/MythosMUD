# Realtime Nats Retry

> 11 nodes · cohesion 0.20

## Key Concepts

- **.retry_async()** (5 connections) — `server/realtime/nats_retry_handler.py`
- **.calculate_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **.retry_with_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **Any** (4 connections) — `server/realtime/nats_retry_handler.py`
- **.get_retry_stats()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **.update_config()** (3 connections) — `server/realtime/nats_retry_handler.py`
- **Calculate exponential backoff delay with jitter.          Args:             atte** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Retry a function with exponential backoff.          Args:             func: Asyn** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Get retry statistics.          Returns:             Dictionary with retry metric** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Retry async function with exponential backoff.          Attempts the function up** (1 connections) — `server/realtime/nats_retry_handler.py`
- **Update retry configuration dynamically.          Allows runtime adjustment of re** (1 connections) — `server/realtime/nats_retry_handler.py`

## Relationships

- [[NATS Retry Handler]] (6 shared connections)

## Source Files

- `server/realtime/nats_retry_handler.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
