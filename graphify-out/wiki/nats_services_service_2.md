# nats services service

> 65 nodes

## Key Concepts

- **test_combat_death_handler.py** (30 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (8 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_player_death_events()** (7 connections) — `server/services/combat_death_handler.py`
- **.handle_target_state_changes()** (6 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **Protocol** (3 connections)
- **.canonical_room_id()** (3 connections) — `server/services/combat_death_handler.py`
- **.get_npc_combat_integration_service()** (3 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (3 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_service()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **handler()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **combat()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **player_target()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- **npc_target()** (2 connections) — `server/tests/unit/services/test_combat_death_handler.py`
- *... and 40 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (14 shared connections)
- [task registry app](task_registry_app.md) (13 shared connections)
- [Item Instances](Item_Instances.md) (9 shared connections)
- [command factories exploration](command_factories_exploration.md) (9 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (7 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (4 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [player persistence repository](player_persistence_repository.md) (1 shared connections)

## Source Files

- `server/services/combat_death_handler.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_combat_death_handler.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 195 (87%)
- INFERRED: 28 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*