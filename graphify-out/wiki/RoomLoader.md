# RoomLoader

> 102 nodes

## Key Concepts

- **test_npc_instance_service.py** (54 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **asyncio** (23 connections)
- **NPCInstanceService** (22 connections) — `server/services/npc_instance_service.py`
- **initialize_npc_instance_service()** (10 connections) — `server/services/npc_instance_service.py`
- **Any** (8 connections)
- **fixture** (8 connections)
- **._extract_zone_from_room_id()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_population_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_zone_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.spawn_npc_instance()** (4 connections) — `server/services/npc_instance_service.py`
- **mock_event_bus()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **mock_lifecycle_manager()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **mock_population_controller()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **mock_spawning_service()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **npc_instance_service()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_get_npc_instances_get_stats_exception()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_initialize_npc_instance_service()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **test_npc_instance_service_init()** (4 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **.despawn_npc_instance()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_npc_instances()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_npc_stats()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_system_stats()** (3 connections) — `server/services/npc_instance_service.py`
- **.move_npc_instance()** (3 connections) — `server/services/npc_instance_service.py`
- **sample_lifecycle_record()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **sample_npc_definition()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- *... and 77 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [test_look_room.py](test_look_room.py.md) (5 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [Invite](Invite.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [mock_connection_manager](mock_connection_manager.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 165 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*