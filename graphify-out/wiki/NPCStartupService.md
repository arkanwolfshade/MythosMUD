# NPCStartupService

> 31 nodes

## Key Concepts

- **NPCStartupService** (52 connections) — `server/services/npc_startup_service.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **Any** (16 connections)
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **.spawn_npcs_on_startup()** (6 connections) — `server/services/npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- **._try_spawn_npc()** (5 connections) — `server/services/npc_startup_service.py`
- **._get_persistence_for_spawn()** (4 connections) — `server/services/npc_startup_service.py`
- **._handle_required_no_room()** (4 connections) — `server/services/npc_startup_service.py`
- **._spawn_one_arena_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **._try_sub_zone_room()** (4 connections) — `server/services/npc_startup_service.py`
- **._warmup_room_cache_for_arena()** (4 connections) — `server/services/npc_startup_service.py`
- **_record_spawned_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **_merge_phase_into_startup()** (3 connections) — `server/services/npc_startup_service.py`
- **._get_default_room_for_sub_zone()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_fallback_room()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_specific_room()** (3 connections) — `server/services/npc_startup_service.py`
- **.__init__()** (2 connections) — `server/services/npc_startup_service.py`
- **Get the singleton container instance.** (1 connections) — `server/container/main.py`
- **Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…** (1 connections) — `server/services/npc_startup_service.py`
- **Spawn optional NPCs based on spawn probability. Args: optional_npcs: List of…** (1 connections) — `server/services/npc_startup_service.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_npc_startup_service.py](test_npc_startup_service.py.md) (33 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (7 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)
- [.connection_manager](connection_manager.md) (3 shared connections)
- [UserManager](UserManager.md) (3 shared connections)
- [CombatDeathHandler](CombatDeathHandler.md) (2 shared connections)
- [HealthService](HealthService.md) (2 shared connections)
- [test_application_container.py](test_application_container.py.md) (2 shared connections)
- [MagicServiceHealingMixin](MagicServiceHealingMixin.md) (1 shared connections)
- [StatsGenerator](StatsGenerator.md) (1 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (1 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/npc_startup_service.py`

## Audit Trail

- EXTRACTED: 104 (76%)
- INFERRED: 32 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*