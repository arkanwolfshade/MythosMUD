# test room subscription manager npcs

> 14 nodes

## Key Concepts

- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_serializes_per_player()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_token_expiry()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_token_ttl_zero()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_enforces_max_tokens()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_cleanup_empty_state()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Unit tests for inventory mutation guard - synchronous acquire operations.  Tests** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Create an InventoryMutationGuard instance.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire serializes mutations per player.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire allows token reuse after expiry.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire with token_ttl=0 (no expiry).** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire enforces max_tokens limit.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **Test acquire cleans up state when tokens are empty.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Relationships

- [Lock](Lock.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 30 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*