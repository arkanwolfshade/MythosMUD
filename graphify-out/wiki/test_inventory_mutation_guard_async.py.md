# test_inventory_mutation_guard_async.py

> 16 nodes

## Key Concepts

- **test_inventory_mutation_guard_async.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **asyncio** (6 connections)
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_cleanup_empty_state()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_concurrent_same_player()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_enforces_max_tokens()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_token_expiry()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_token_ttl_zero()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **fixture** (1 connections)
- **Unit tests for inventory mutation guard - asynchronous acquire operations.…** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async serializes concurrent mutations for same player.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Create an InventoryMutationGuard instance.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async enforces max_tokens limit.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async allows token reuse after expiry.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async with token_ttl=0 (no expiry).** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Test acquire_async cleans up state when tokens are empty.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`

## Relationships

- [server/services/__init__.py](server-services-__init__.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_inventory_mutation_guard_async.py`

## Audit Trail

- EXTRACTED: 23 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*