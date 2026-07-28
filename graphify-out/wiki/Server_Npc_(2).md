# Server Npc (2)

> 194 nodes

## Key Concepts

- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **time_event_consumer.py** (24 connections) — `server/time/time_event_consumer.py`
- **NPCThreadManager** (22 connections) — `server/npc/threading.py`
- **MythosTimeEventConsumer** (21 connections) — `server/time/time_event_consumer.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_periodic.py** (18 connections) — `server/npc/lifecycle_periodic.py`
- **_SpawnTrackedNPC** (17 connections) — `server/npc/lifecycle_manager.py`
- **NPCLifecycleRecord** (17 connections) — `server/npc/lifecycle_types.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- **._spawn_npc_impl()** (14 connections) — `server/npc/lifecycle_manager.py`
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **lifecycle_types.py** (12 connections) — `server/npc/lifecycle_types.py`
- **NPCLifecycleState** (12 connections) — `server/npc/lifecycle_types.py`
- **MythosHourTickEvent** (12 connections) — `server/events/event_types.py`
- **NPCLifecycleEvent** (11 connections) — `server/npc/lifecycle_types.py`
- **lifecycle_despawn.py** (10 connections) — `server/npc/lifecycle_despawn.py`
- **lifecycle_respawn.py** (9 connections) — `server/npc/lifecycle_respawn.py`
- **NPCMaintenanceConfig** (8 connections) — `server/config/npc_config.py`
- **Any** (8 connections)
- **check_optional_npc_spawns_impl()** (8 connections) — `server/npc/lifecycle_periodic.py`
- **.__init__()** (8 connections) — `server/time/time_event_consumer.py`
- **._finalize_spawn_record()** (7 connections) — `server/npc/lifecycle_manager.py`
- **run_periodic_maintenance_impl()** (7 connections) — `server/npc/lifecycle_periodic.py`
- **process_respawn_queue_impl()** (7 connections) — `server/npc/lifecycle_respawn.py`
- *... and 169 more nodes in this community*

## Relationships

- [Server Events](Server_Events.md) (60 shared connections)
- [Server Npc](Server_Npc.md) (41 shared connections)
- [Server Commands](Server_Commands.md) (22 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (17 shared connections)
- [Server App](Server_App.md) (7 shared connections)
- [Server Services (15)](Server_Services_%2815%29.md) (7 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (6 shared connections)
- [Server Npc (3)](Server_Npc_%283%29.md) (6 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (6 shared connections)
- [Server Time](Server_Time.md) (5 shared connections)
- [Server App (2)](Server_App_%282%29.md) (4 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (4 shared connections)

## Source Files

- `server/config/npc_config.py`
- `server/container/bundles/time.py`
- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_periodic.py`
- `server/npc/lifecycle_respawn.py`
- `server/npc/lifecycle_types.py`
- `server/npc/threading.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_npc_instance_service.py`
- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 713 (88%)
- INFERRED: 94 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*