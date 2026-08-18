# server npc shopkeeper npc rationale

> 21 nodes

## Key Concepts

- **ShopkeeperNPC** (19 connections) — `server/npc/shopkeeper_npc.py`
- **.__init__()** (3 connections) — `server/npc/shopkeeper_npc.py`
- **._setup_shopkeeper_behavior_rules()** (3 connections) — `server/npc/shopkeeper_npc.py`
- **.add_buyable_item()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.add_shop_item()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.buy_from_player()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.calculate_price()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **._handle_greet_customer()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **._handle_restock_inventory()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.get_shop_inventory()** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Buy item from player.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Calculate final price with markup.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Handle greeting customer action.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Handle restocking inventory action.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Shopkeeper NPC type with buy/sell functionality.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Initialize shopkeeper NPC.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Setup shopkeeper-specific behavior rules.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Get shopkeeper-specific behavior rules.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Add item to shop inventory.** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Add item to buyable items list.** (1 connections) — `server/npc/shopkeeper_npc.py`

## Relationships

- [server npc shopkeeper npc rationale](server_npc_shopkeeper_npc_rationale.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (2 shared connections)

## Source Files

- `server/npc/shopkeeper_npc.py`

## Audit Trail

- EXTRACTED: 28 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*