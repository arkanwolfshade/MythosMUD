# NPCBase

> 80 nodes

## Key Concepts

- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **_PopulationLifecycleManager** (6 connections) — `server/npc/population_control.py`
- **._create_npc_instance()** (6 connections) — `server/npc/spawning_service.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **._handle_npc_death()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **.execute_behavior()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **._enrich_behavior_context()** (3 connections) — `server/npc/npc_base.py`
- **.from_dict()** (3 connections) — `server/npc/npc_base.py`
- **.get_combat_stats()** (3 connections) — `server/npc/npc_base.py`
- **._is_npc_in_combat()** (3 connections) — `server/npc/npc_base.py`
- **.listen()** (3 connections) — `server/npc/npc_base.py`
- **._move_simple()** (3 connections) — `server/npc/npc_base.py`
- **._safe_stat_int()** (3 connections) — `server/npc/npc_base.py`
- **.schedule_idle_movement()** (3 connections) — `server/npc/npc_base.py`
- **._setup_base_behavior_rules()** (3 connections) — `server/npc/npc_base.py`
- **.speak()** (3 connections) — `server/npc/npc_base.py`
- **._sync_dp_stats()** (3 connections) — `server/npc/npc_base.py`
- *... and 55 more nodes in this community*

## Relationships

- [npc_base.py](npc_base.py.md) (18 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (7 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [NPCDied](NPCDied.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (2 shared connections)
- [CommunicationIntegrationProtocol](CommunicationIntegrationProtocol.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (2 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`

## Audit Trail

- EXTRACTED: 139 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*