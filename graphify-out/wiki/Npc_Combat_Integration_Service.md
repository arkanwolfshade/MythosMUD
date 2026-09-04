# Npc Combat Integration Service

> 40 nodes

## Key Concepts

- **NPCCombatIntegrationService** (86 connections) — `server/services/npc_combat_integration_service.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.get_combat_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_data_provider()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_lucidity_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_messaging_integration()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_rewards_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_uuid_mapping()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **._init_player_combat_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.clear_npc_combat_memory()** (2 connections) — `server/services/npc_combat_integration_service.py`
- **.get_npc_combat_memory()** (2 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_death()** (2 connections) — `server/services/npc_combat_integration_service.py`
- **ConnectionManager** (2 connections)
- **UUID** (2 connections)
- **Return combat messaging integration for room broadcasts (e.g. aggro switches).** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Return combat service dependency for integration collaborators.** (1 connections) — `server/services/npc_combat_integration_service.py`
- *... and 15 more nodes in this community*

## Relationships

- [Test Npc Combat Integration Service](Test_Npc_Combat_Integration_Service.md) (37 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (18 shared connections)
- [Npc Base](Npc_Base.md) (4 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (4 shared connections)
- [Combat Taunt](Combat_Taunt.md) (3 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (3 shared connections)
- [Combat Events](Combat_Events.md) (3 shared connections)
- [Test Player Combat Service](Test_Player_Combat_Service.md) (3 shared connections)
- [Test Npc Combat Lucidity](Test_Npc_Combat_Lucidity.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Npc Combat Grace](Npc_Combat_Grace.md) (2 shared connections)
- [Async Persistence](Async_Persistence.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 88 (64%)
- INFERRED: 49 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*