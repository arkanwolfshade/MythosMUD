# grace period disconnect

> 26 nodes

## Key Concepts

- **test_shopkeeper_npc.py** (25 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **_shopkeeper()** (20 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **_shop_quantity()** (5 connections) — `server/npc/shopkeeper_npc.py`
- **test_add_buyable_item_invalid()** (3 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **.sell_to_player()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **test_shop_quantity_coercion()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_add_shop_item_and_inventory()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_add_buyable_item()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_buy_from_player_success()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_buy_from_player_not_buyable()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_sell_to_player_reduces_quantity()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_sell_to_player_removes_depleted_item()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_sell_to_player_not_available()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_calculate_price_default_markup()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_calculate_price_explicit_markup()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_behavior_handlers()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_get_behavior_rules()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_add_shop_item_invalid_item()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_buy_from_player_inventory_failure()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_buy_from_player_exception()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_sell_to_player_insufficient_quantity()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_sell_to_player_exception()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_calculate_price_invalid_markup_config()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **test_get_shop_inventory_returns_copy()** (2 connections) — `server/tests/unit/npc/test_shopkeeper_npc.py`
- **Coerce inventory quantity from JSON-shaped dict values to int (excludes bool).** (1 connections) — `server/npc/shopkeeper_npc.py`
- *... and 1 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/npc/shopkeeper_npc.py`
- `server/tests/unit/npc/test_shopkeeper_npc.py`

## Audit Trail

- EXTRACTED: 94 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*