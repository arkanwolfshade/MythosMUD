# Combat Integration Base

> 58 nodes

## Key Concepts

- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_base.py** (23 connections) — `server/npc/combat_integration_base.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **.apply_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **._convert_target_id_to_uuid()** (6 connections) — `server/npc/combat_integration_base.py`
- **._handle_npc_attack_core()** (6 connections) — `server/npc/combat_integration_base.py`
- **.__init__()** (5 connections) — `server/npc/combat_integration_base.py`
- **._try_delegate_npc_attack_to_combat_service()** (5 connections) — `server/npc/combat_integration_base.py`
- **._handle_attribute_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_unexpected_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._handle_validation_error()** (4 connections) — `server/npc/combat_integration_base.py`
- **._apply_mental_effects()** (3 connections) — `server/npc/combat_integration_base.py`
- **.calculate_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_npc_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._get_target_stats()** (3 connections) — `server/npc/combat_integration_base.py`
- **.handle_npc_attack()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_npc_attack_to_nats()** (3 connections) — `server/npc/combat_integration_base.py`
- **._publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/npc/combat_integration_base.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- *... and 33 more nodes in this community*

## Relationships

- [Test Npc Combat Integration Class](Test_Npc_Combat_Integration_Class.md) (10 shared connections)
- [Game State Provider](Game_State_Provider.md) (9 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (6 shared connections)
- [Combat Events](Combat_Events.md) (5 shared connections)
- [Test Config Init](Test_Config_Init.md) (3 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (3 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (2 shared connections)
- [Mechanics](Mechanics.md) (2 shared connections)
- [Async Persistence](Async_Persistence.md) (2 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (2 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 135 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*