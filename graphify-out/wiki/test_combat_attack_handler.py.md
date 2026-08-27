# test_combat_attack_handler.py

> 61 nodes

## Key Concepts

- **NPCPopulationController** (55 connections) — `server/npc/population_control.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **_PopulationLifecycleManager** (6 connections) — `server/npc/population_control.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (6 connections) — `server/npc/population_control.py`
- **.__init__()** (6 connections) — `server/services/npc_instance_service.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.is_required()** (4 connections) — `server/models/npc.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- **.get_zone_configuration()** (4 connections) — `server/npc/population_control.py`
- **._handle_player_left_room()** (4 connections) — `server/npc/population_control.py`
- **._load_zone_configurations()** (4 connections) — `server/npc/population_control.py`
- **._update_player_count()** (4 connections) — `server/npc/population_control.py`
- **.clear_population_stats()** (3 connections) — `server/npc/population_control.py`
- **.get_zone_population_summary()** (3 connections) — `server/npc/population_control.py`
- **._handle_npc_entered_room()** (3 connections) — `server/npc/population_control.py`
- **._handle_npc_left_room()** (3 connections) — `server/npc/population_control.py`
- **.load_npc_definitions()** (3 connections) — `server/npc/population_control.py`
- **._subscribe_to_events()** (3 connections) — `server/npc/population_control.py`
- *... and 36 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (20 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (8 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [RoomLoader](RoomLoader.md) (5 shared connections)
- [ErrorType](ErrorType.md) (4 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (4 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (4 shared connections)
- [Invite](Invite.md) (3 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (1 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/population_control.py`
- `server/services/npc_instance_service.py`
- `server/tests/unit/npc/test_population_control.py`

## Audit Trail

- EXTRACTED: 119 (87%)
- INFERRED: 18 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*