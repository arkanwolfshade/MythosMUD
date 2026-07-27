# Services Inventory Mutation

> 24 nodes · cohesion 0.09

## Key Concepts

- **test_inventory_mutation_guard_async.py** (8 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_inventory_mutation_guard_sync.py** (8 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_async_cleanup_empty_state()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_concurrent_same_player()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_enforces_max_tokens()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_token_expiry()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_token_ttl_zero()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Unit tests for inventory mutation guard - synchronous acquire operations.  Tests** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire allows token reuse after expiry.** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire with token_ttl=0 (no expiry).** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire enforces max_tokens limit.** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_cleanup_empty_state()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_enforces_max_tokens()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_serializes_per_player()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_token_expiry()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_token_ttl_zero()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire_async serializes concurrent mutations for same player.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Create an InventoryMutationGuard instance.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async cleans up state when tokens are empty.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Create an InventoryMutationGuard instance.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire serializes mutations per player.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire cleans up state when tokens are empty.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Relationships

- [[Inventory Service Helpers]] (4 shared connections)

## Source Files

- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
