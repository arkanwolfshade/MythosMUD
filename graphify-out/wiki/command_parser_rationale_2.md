# command parser rationale

> 169 nodes

## Key Concepts

- **NPCLifecycleManager** (78 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_manager.py** (49 connections) — `server/npc/lifecycle_manager.py`
- **NPCDied** (35 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **NPCLifecycleRecord** (19 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_despawn.py** (19 connections) — `server/tests/unit/npc/test_lifecycle_despawn.py`
- **despawn_npc_impl()** (18 connections) — `server/npc/lifecycle_despawn.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **RoomOccupantsRefreshRequested** (17 connections) — `server/events/event_types.py`
- **_SpawnTrackedNPC** (17 connections) — `server/npc/lifecycle_manager.py`
- **NPCLifecycleState** (17 connections) — `server/npc/lifecycle_types.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **lifecycle_despawn.py** (16 connections) — `server/npc/lifecycle_despawn.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_types.py** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_lifespan_event_subscriptions.py** (15 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **._spawn_npc_impl()** (14 connections) — `server/npc/lifecycle_manager.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **lifespan_event_subscriptions.py** (12 connections) — `server/app/lifespan_event_subscriptions.py`
- **NPCLifecycleEvent** (12 connections) — `server/npc/lifecycle_types.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- *... and 144 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (68 shared connections)
- [models npc rationale](models_npc_rationale.md) (40 shared connections)
- [Loot Generation](Loot_Generation.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (11 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (10 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (9 shared connections)
- [npc lifecycle config](npc_lifecycle_config.md) (8 shared connections)
- [combat services rationale](combat_services_rationale.md) (6 shared connections)
- [player death service](player_death_service.md) (5 shared connections)
- [follow game service](follow_game_service.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_despawn.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 774 (89%)
- INFERRED: 98 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*