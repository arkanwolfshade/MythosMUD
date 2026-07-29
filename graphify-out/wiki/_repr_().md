# . repr ()

> 318 nodes

## Key Concepts

- **NPCDefinition** (115 connections) — `server/models/npc.py`
- **NPCLifecycleManager** (70 connections) — `server/npc/lifecycle_manager.py`
- **NPCSpawnRule** (55 connections) — `server/models/npc.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **npc.py** (37 connections) — `server/models/npc.py`
- **test_npc_models.py** (33 connections) — `server/tests/unit/models/test_npc_models.py`
- **NPCDied** (25 connections) — `server/events/event_types.py`
- **test_spawn_validator.py** (24 connections) — `server/tests/unit/npc/test_spawn_validator.py`
- **lifecycle_death.py** (23 connections) — `server/npc/lifecycle_death.py`
- **should_spawn_npc()** (22 connections) — `server/npc/spawn_validator.py`
- **NPCThreadManager** (22 connections) — `server/npc/threading.py`
- **_SpawnTrackedNPC** (17 connections) — `server/npc/lifecycle_manager.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **._spawn_npc_impl()** (14 connections) — `server/npc/lifecycle_manager.py`
- **combat_schema.py** (13 connections) — `server/schemas/combat/combat_schema.py`
- **lifecycle_types.py** (12 connections) — `server/npc/lifecycle_types.py`
- **NPCLifecycleState** (12 connections) — `server/npc/lifecycle_types.py`
- **NPCLifecycleEvent** (11 connections) — `server/npc/lifecycle_types.py`
- **spawn_validator.py** (11 connections) — `server/npc/spawn_validator.py`
- **_JSONDict** (10 connections)
- *... and 293 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (95 shared connections)
- [Any](Any.md) (59 shared connections)
- [main()](main%28%29.md) (37 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (21 shared connections)
- [.is required()](is_required%28%29.md) (13 shared connections)
- [.set player combat service()](set_player_combat_service%28%29.md) (11 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (10 shared connections)
- [. init ()](_init_%28%29.md) (9 shared connections)
- [Represents the configuration for a](Represents_the_configuration_for_a.md) (9 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (7 shared connections)
- [test npc event handlers](test_npc_event_handlers.md) (6 shared connections)
- [. post init ()](_post_init_%28%29.md) (5 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/npc.py`
- `server/models/room.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/population_control.py`
- `server/npc/spawn_validator.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_service.py`
- `server/npc/threading.py`
- `server/realtime/event_handler.py`
- `server/schemas/combat/combat_schema.py`
- `server/tests/unit/models/test_npc_models.py`
- `server/tests/unit/npc/test_spawn_validator.py`

## Audit Trail

- EXTRACTED: 1271 (90%)
- INFERRED: 139 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*