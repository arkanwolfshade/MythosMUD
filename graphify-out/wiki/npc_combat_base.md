# npc combat base

> 47 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **._handle_attribute_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_validation_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_unexpected_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **.handle_npc_attack()** (4 connections) — `server/npc/combat_integration_base.py`
- **._get_target_stats()** (4 connections) — `server/npc/combat_integration_base.py`
- **.calculate_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **UUID** (3 connections)
- **._apply_mental_effects()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_npc_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_npc_attack_to_nats()** (3 connections) — `server/npc/combat_integration_base.py`
- **ABC** (2 connections)
- **Protocol** (2 connections)
- **.handle_npc_attack_on_player()** (2 connections) — `server/npc/combat_integration_protocols.py`
- **ValidationError** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (4 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [realtime game state](realtime_game_state.md) (2 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [command commands aliases](command_commands_aliases.md) (1 shared connections)
- [message queue realtime](message_queue_realtime.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 145 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*