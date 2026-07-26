# NPCBase

> 80 nodes · cohesion 0.03

## Key Concepts

- **NPCBase** (82 connections) — `server/npc/npc_base.py`
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
- *... and 55 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (23 shared connections)
- [npc_base.py](npc_base.py.md) (13 shared connections)
- [npc_config_parsing.py](npc_config_parsing.py.md) (7 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (2 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (2 shared connections)
- [.despawn_npc](despawn_npc.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [QuestService](QuestService.md) (1 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_protocols.py`

## Audit Trail

- EXTRACTED: 225 (89%)
- INFERRED: 27 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*