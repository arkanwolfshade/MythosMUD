# NPCBase

> 157 nodes

## Key Concepts

- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **CommunicationIntegrationProtocol** (8 connections) — `server/npc/npc_protocols.py`
- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **CombatIntegrationProtocol** (6 connections) — `server/npc/npc_protocols.py`
- **_PopulationLifecycleManager** (6 connections) — `server/npc/population_control.py`
- **._finalize_spawn_record()** (6 connections) — `server/npc/lifecycle_manager.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **_SpawningServiceProtocol** (5 connections) — `server/npc/lifecycle_manager.py`
- **_SpawnTrackedNPC** (5 connections) — `server/npc/lifecycle_manager.py`
- **._handle_npc_death()** (5 connections) — `server/npc/npc_base.py`
- **.is_alive()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (5 connections) — `server/npc/npc_base.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **test_npc_combat_schedule.py** (5 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- *... and 132 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (57 shared connections)
- [NPCDied](NPCDied.md) (3 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (3 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [._init_player_quest_layer](_init_player_quest_layer.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (2 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (1 shared connections)
- [.add_item_to_inventory](add_item_to_inventory.md) (1 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (1 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (1 shared connections)
- [ShopkeeperNPC](ShopkeeperNPC.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/npc.py`
- `server/npc/idle_movement.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_protocols.py`
- `server/npc/population_control.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 257 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*