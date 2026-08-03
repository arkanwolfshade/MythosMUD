# npc combat player

> 14 nodes

## Key Concepts

- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_enforces_max_tokens()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_token_expiry()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_token_ttl_zero()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_cleanup_empty_state()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_concurrent_same_player()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Unit tests for inventory mutation guard - asynchronous acquire operations.  Test** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Create an InventoryMutationGuard instance.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async enforces max_tokens limit.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async allows token reuse after expiry.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async with token_ttl=0 (no expiry).** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async cleans up state when tokens are empty.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async serializes concurrent mutations for same player.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)

## Source Files

- `server/tests/unit/services/test_inventory_mutation_guard_async.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*