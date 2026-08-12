# .acquire

> 29 nodes

## Key Concepts

- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._emit_duplicate_mutation_alert()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **.get_lock()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **Acquire sync mutation guard.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Acquire async mutation guard.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create per-player guard state for sync contexts. Uses thread-safe…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create per-player guard state for async contexts. Uses async lock to…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Clean up per-player guard state when no longer needed (sync context). Removes…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Clean up per-player guard state when no longer needed (async context). Removes…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Remove expired idempotency tokens from the guard state (sync context). Tokens…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Remove expired idempotency tokens from the guard state (async context). Tokens…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Enforce maximum token cache size by removing oldest entries (sync context).…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Enforce maximum token cache size by removing oldest entries (async context).…** (1 connections) — `server/services/inventory_mutation_guard.py`
- *... and 4 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (12 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 85 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*