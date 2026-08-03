# player event handlers

> 22 nodes

## Key Concepts

- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (9 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **.get_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **.__init__()** (3 connections) — `server/container/main.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (2 connections) — `server/services/inventory_mutation_guard.py`
- **Initialize the container. Services are NOT initialized here - use initialize().** (1 connections) — `server/container/main.py`
- **Initialize metrics collector.          AI: Uses Lock for thread-safety in async** (1 connections) — `server/middleware/metrics_collector.py`
- **Internal state tracking per-player mutation metadata for async contexts.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create the async lock (lazy initialization).** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create the async global lock (lazy initialization).** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Acquire a mutation context for the given player and token (async version).** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create per-player guard state for async contexts.          Uses async loc** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Clean up per-player guard state when no longer needed (async context).** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Remove expired idempotency tokens from the guard state (async context).** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Enforce maximum token cache size by removing oldest entries (async context).** (1 connections) — `server/services/inventory_mutation_guard.py`

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (10 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (1 shared connections)
- [combat service services](combat_service_services.md) (1 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (1 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)
- [health models rationale](health_models_rationale.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/middleware/metrics_collector.py`
- `server/services/inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 63 (88%)
- INFERRED: 9 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*