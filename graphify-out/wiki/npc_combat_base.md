# npc combat base

> 47 nodes

## Key Concepts

- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_base.py** (21 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
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
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **ABC** (2 connections)
- **Protocol** (2 connections)
- **.handle_npc_attack_on_player()** (2 connections) — `server/npc/combat_integration_protocols.py`
- **ValidationError** (1 connections)
- *... and 22 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (13 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [room persistence loader](room_persistence_loader.md) (2 shared connections)
- [services nats service](services_nats_service.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [message queue realtime](message_queue_realtime.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 156 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*