# Npc Base

> 96 nodes

## Key Concepts

- **NPCBase** (72 connections) — `server/npc/npc_base.py`
- **spawning_instance_factory.py** (25 connections) — `server/npc/spawning_instance_factory.py`
- **SimpleNPCDefinition** (16 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (16 connections) — `server/npc/spawning_instance_factory.py`
- **generate_npc_id()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **._handle_npc_death()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **_coerce_simple_definition()** (5 connections) — `server/npc/spawning_instance_factory.py`
- **._generate_npc_id()** (5 connections) — `server/npc/spawning_service.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **.execute_behavior()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **.is_required()** (3 connections) — `server/models/npc.py`
- **._enrich_behavior_context()** (3 connections) — `server/npc/npc_base.py`
- *... and 71 more nodes in this community*

## Relationships

- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (27 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (18 shared connections)
- [NPC Models](NPC_Models.md) (8 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (8 shared connections)
- [Test Npc Combat Integration Class](Test_Npc_Combat_Integration_Class.md) (5 shared connections)
- [Test Npc Utils](Test_Npc_Utils.md) (4 shared connections)
- [Npc Combat Integration Service](Npc_Combat_Integration_Service.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Target Resolution Service](Test_Target_Resolution_Service.md) (2 shared connections)
- [Shopkeeper Npc](Shopkeeper_Npc.md) (2 shared connections)
- [Test Lifespan Event Subscriptions](Test_Lifespan_Event_Subscriptions.md) (2 shared connections)
- [Test Behavior Engine](Test_Behavior_Engine.md) (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/tests/unit/npc/test_spawning_modules.py`

## Audit Trail

- EXTRACTED: 193 (86%)
- INFERRED: 31 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*