# Character Creation API

> 50 nodes · cohesion 0.03

## Key Concepts

- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **.execute_behavior()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **.listen()** (4 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **.speak()** (4 connections) — `server/npc/npc_base.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **._enrich_behavior_context()** (3 connections) — `server/npc/npc_base.py`
- **.from_dict()** (3 connections) — `server/npc/npc_base.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **.get_stats()** (3 connections) — `server/npc/npc_base.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/npc_base.py`
- **._move_simple()** (3 connections) — `server/npc/npc_base.py`
- **.schedule_idle_movement()** (3 connections) — `server/npc/npc_base.py`
- **._sync_dp_stats()** (3 connections) — `server/npc/npc_base.py`
- **._update_determination_points()** (3 connections) — `server/npc/npc_base.py`
- **.generate_ai_response()** (2 connections) — `server/npc/npc_base.py`
- *... and 25 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (23 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (13 shared connections)
- [Test Optimization Roadmap](Test_Optimization_Roadmap.md) (8 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (2 shared connections)
- [NPC Definition Schemas](NPC_Definition_Schemas.md) (2 shared connections)
- [NPC Movement Integration](NPC_Movement_Integration.md) (2 shared connections)
- [Facades Implementation Summary](Facades_Implementation_Summary.md) (2 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (1 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)
- [App Router Integration](App_Router_Integration.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_protocols.py`

## Audit Trail

- EXTRACTED: 196 (88%)
- INFERRED: 27 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*