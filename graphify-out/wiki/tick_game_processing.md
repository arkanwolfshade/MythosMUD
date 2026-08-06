# tick game processing

> 91 nodes

## Key Concepts

- **test_combat_death_handler.py** (30 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (9 connections) — `server/services/combat_death_handler.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (8 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (6 connections) — `server/services/combat_death_handler.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.check_connection_state()** (5 connections) — `server/services/combat_cleanup_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **ContainerComponent** (5 connections)
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.can_access_corpse()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 66 more nodes in this community*

## Relationships

- [task registry app](task_registry_app.md) (13 shared connections)
- [models npc rationale](models_npc_rationale.md) (12 shared connections)
- [game chat service](game_chat_service.md) (9 shared connections)
- [Item Instances](Item_Instances.md) (9 shared connections)
- [command factories exploration](command_factories_exploration.md) (9 shared connections)
- [player event handlers](player_event_handlers.md) (5 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [realtime player connection](realtime_player_connection.md) (4 shared connections)
- [subject admin controller](subject_admin_controller.md) (3 shared connections)
- [commands communication support](commands_communication_support.md) (3 shared connections)
- [player event realtime](player_event_realtime.md) (2 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (2 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_combat_death_handler.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 262 (84%)
- INFERRED: 49 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*