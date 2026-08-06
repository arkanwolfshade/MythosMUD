# event connection helpers

> 34 nodes

## Key Concepts

- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (9 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.get_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **.__init__()** (3 connections) — `server/container/main.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.__init__()** (2 connections) — `server/services/inventory_mutation_guard.py`
- **Initialize the container. Services are NOT initialized here - use initialize().** (1 connections) — `server/container/main.py`
- **Initialize metrics collector.          AI: Uses Lock for thread-safety in async** (1 connections) — `server/middleware/metrics_collector.py`
- **Initialize the communication bridge.** (1 connections) — `server/npc/threading.py`
- **Internal state tracking per-player mutation metadata.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Internal state tracking per-player mutation metadata for async contexts.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create the async lock (lazy initialization).** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create the async global lock (lazy initialization).** (1 connections) — `server/services/inventory_mutation_guard.py`
- *... and 9 more nodes in this community*

## Relationships

- [task registry app](task_registry_app.md) (14 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [room cache services](room_cache_services.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (1 shared connections)
- [spell models rationale](spell_models_rationale.md) (1 shared connections)
- [rate limiter services](rate_limiter_services.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 97 (90%)
- INFERRED: 11 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*