# Server Npc (3)

> 158 nodes

## Key Concepts

- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **npc_config_parsing.py** (14 connections) — `server/npc/npc_config_parsing.py`
- **NPCSpawnResult** (14 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (12 connections) — `server/npc/spawning_request_execution.py`
- **.__init__()** (11 connections) — `server/npc/npc_base.py`
- **CommunicationIntegrationProtocol** (10 connections) — `server/npc/npc_protocols.py`
- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **to_int_or_default()** (7 connections) — `server/npc/npc_config_parsing.py`
- **get_combat_stats_dict()** (7 connections) — `server/npc/npc_config_parsing.py`
- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **._get_active_npcs_from_lifecycle_manager()** (6 connections) — `server/npc/population_control.py`
- **._spawn_npc_from_request()** (6 connections) — `server/npc/spawning_service.py`
- **._register_reactions_and_chat_name()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **normalize_determination_points()** (5 connections) — `server/npc/npc_config_parsing.py`
- **parse_behavior_config()** (5 connections) — `server/npc/npc_config_parsing.py`
- **_safe_stat_int()** (5 connections) — `server/npc/npc_config_parsing.py`
- **._should_remove_inactive_npc()** (5 connections) — `server/npc/population_control.py`
- **.cleanup_inactive_npcs()** (5 connections) — `server/npc/population_control.py`
- **_spawn_success()** (5 connections) — `server/npc/spawning_request_execution.py`
- **.get_spawn_statistics()** (5 connections) — `server/npc/spawning_service.py`
- **._get_npc_instance()** (5 connections) — `server/services/target_resolution_service.py`
- *... and 133 more nodes in this community*

## Relationships

- [Server Npc](Server_Npc.md) (34 shared connections)
- [Server Events](Server_Events.md) (31 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (6 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Npc (7)](Server_Npc_%287%29.md) (3 shared connections)
- [Server Npc (14)](Server_Npc_%2814%29.md) (3 shared connections)
- [Server App](Server_App.md) (3 shared connections)
- [Server Services (12)](Server_Services_%2812%29.md) (3 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (3 shared connections)
- [Server Npc (5)](Server_Npc_%285%29.md) (2 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (2 shared connections)
- [Server Models (6)](Server_Models_%286%29.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/npc/npc_config_parsing.py`
- `server/npc/npc_protocols.py`
- `server/npc/population_control.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 464 (93%)
- INFERRED: 34 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*