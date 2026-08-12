# Active Lucidity Service

> 34 nodes

## Key Concepts

- **NPCEventReactionSystem** (21 connections) — `server/npc/event_reaction_system.py`
- **ShopkeeperNPC** (17 connections) — `server/npc/shopkeeper_npc.py`
- **shopkeeper_npc.py** (11 connections) — `server/npc/shopkeeper_npc.py`
- **.__init__()** (4 connections) — `server/npc/event_reaction_system.py`
- **.register_npc_reactions()** (3 connections) — `server/npc/event_reaction_system.py`
- **_shop_quantity()** (3 connections) — `server/npc/shopkeeper_npc.py`
- **.__init__()** (3 connections) — `server/npc/shopkeeper_npc.py`
- **._setup_shopkeeper_behavior_rules()** (3 connections) — `server/npc/shopkeeper_npc.py`
- **.unregister_npc_reactions()** (2 connections) — `server/npc/event_reaction_system.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.add_shop_item()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.add_buyable_item()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.buy_from_player()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.sell_to_player()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **.calculate_price()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **._handle_greet_customer()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **._handle_restock_inventory()** (2 connections) — `server/npc/shopkeeper_npc.py`
- **System for managing NPC event subscriptions and reactions.      This class handl** (1 connections) — `server/npc/event_reaction_system.py`
- **Initialize the NPC event reaction system.          Args:             event_bus:** (1 connections) — `server/npc/event_reaction_system.py`
- **Register reactions for a specific NPC.          Args:             npc_id: The ID** (1 connections) — `server/npc/event_reaction_system.py`
- **Unregister all reactions for a specific NPC.          Args:             npc_id:** (1 connections) — `server/npc/event_reaction_system.py`
- **.get_shop_inventory()** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Shopkeeper NPC type for MythosMUD.  This module provides the ShopkeeperNPC cla** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Coerce inventory quantity from JSON-shaped dict values to int (excludes bool).** (1 connections) — `server/npc/shopkeeper_npc.py`
- **Shopkeeper NPC type with buy/sell functionality.** (1 connections) — `server/npc/shopkeeper_npc.py`
- *... and 9 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (4 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [Player Position Service](Player_Position_Service.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/npc/event_reaction_system.py`
- `server/npc/shopkeeper_npc.py`

## Audit Trail

- EXTRACTED: 92 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*