# Services Inventory Mutation

> 22 nodes · cohesion 0.10

## Key Concepts

- **test_inventory_mutation_guard_internal.py** (13 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Test _prune_tokens with token_ttl=0 doesn't prune.** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Test _enforce_limit removes oldest tokens when limit exceeded.** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_cleanup_async_state_empty()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_cleanup_async_state_locked()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_enforce_limit()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_enforce_limit_async()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_get_async_global_lock()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_get_async_state_creates_lazily()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_prune_tokens()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_prune_tokens_async()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_prune_tokens_async_ttl_zero()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_prune_tokens_ttl_zero()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Unit tests for inventory mutation guard - internal helper methods.  Tests intern** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Test _cleanup_async_state removes empty state.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Test _prune_tokens_async removes expired tokens.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Create an InventoryMutationGuard instance.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Test _prune_tokens removes expired tokens.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Test _get_async_global_lock creates lock lazily.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Test _get_async_state creates state lazily.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **Test _cleanup_async_state handles locked state.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`

## Relationships

- [[Inventory Service Helpers]] (2 shared connections)

## Source Files

- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
