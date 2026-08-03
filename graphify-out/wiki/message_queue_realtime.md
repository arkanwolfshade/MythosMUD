# message queue realtime

> 43 nodes

## Key Concepts

- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **UUID** (7 connections)
- **.get_combat_stats()** (7 connections) — `server/npc/combat_integration.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_for_dp_update()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_and_stats_for_nats()** (4 connections) — `server/npc/combat_integration.py`
- **.handle_npc_death()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._derive_npc_name_from_id()** (3 connections) — `server/npc/combat_integration.py`
- **._normalize_npc_stats()** (3 connections) — `server/npc/combat_integration.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **.get_stats()** (3 connections) — `server/npc/npc_base.py`
- **Resolve NPC instance display name from lifecycle manager, or derive from npc_id.** (1 connections) — `server/npc/combat_integration.py`
- **Best-effort lookup of NPC name from the lifecycle manager.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the NPC lifecycle manager from the app state, if available.** (1 connections) — `server/npc/combat_integration.py`
- *... and 18 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (21 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [realtime game state](realtime_game_state.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [item models rationale](item_models_rationale.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [npc combat base](npc_combat_base.md) (1 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 122 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*