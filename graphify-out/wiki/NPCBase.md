# NPCBase

> 122 nodes

## Key Concepts

- **NPCBase** (79 connections) — `server/npc/npc_base.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **CommunicationIntegrationProtocol** (8 connections) — `server/npc/npc_protocols.py`
- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **CombatIntegrationProtocol** (6 connections) — `server/npc/npc_protocols.py`
- **._handle_npc_death()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (5 connections) — `server/npc/npc_base.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **test_npc_combat_schedule.py** (5 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **._apply_definition_attributes()** (4 connections) — `server/npc/npc_base.py`
- **.execute_behavior()** (4 connections) — `server/npc/npc_base.py`
- **.heal()** (4 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._safe_get()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **_compute_max_dp()** (4 connections) — `server/npc/npc_config_parsing.py`
- **parse_ai_config()** (4 connections) — `server/npc/npc_config_parsing.py`
- *... and 97 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (16 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (10 shared connections)
- [population_control.py](population_control.py.md) (4 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (3 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [BehaviorEngine](BehaviorEngine.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (2 shared connections)
- [.get_instance](get_instance.md) (2 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_protocols.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 210 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*