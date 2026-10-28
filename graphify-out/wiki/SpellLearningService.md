# SpellLearningService

> 98 nodes · cohesion 0.04

## Key Concepts

- **NPCDied** (29 connections) — `server/events/event_types.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **test_quest_events.py** (17 connections) — `server/tests/unit/game/test_quest_events.py`
- **NPCLifecycleRecord** (16 connections) — `server/npc/lifecycle_types.py`
- **test_lifespan_event_subscriptions.py** (16 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **RoomOccupantsRefreshRequested** (14 connections) — `server/events/event_types.py`
- **lifespan_event_subscriptions.py** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **_LifecycleManagerForDeath** (12 connections) — `server/npc/lifecycle_death.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_mark_despawned_and_queue_respawn()** (10 connections) — `server/npc/lifecycle_death.py`
- **_make_on_player_entered()** (8 connections) — `server/game/quest/quest_events.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **_make_on_npc_died()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_player_left()** (7 connections) — `server/game/quest/quest_events.py`
- **test_quest_log_updated_event_envelope_shape()** (6 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **asyncio** (6 connections)
- **test_handle_npc_died_impl_full_path()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **test_mark_despawned_logs_failure()** (6 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **.add_event()** (5 connections) — `server/npc/lifecycle_types.py`
- *... and 73 more nodes in this community*

## Relationships

- [BaseEvent](BaseEvent.md) (27 shared connections)
- [CombatInstance](CombatInstance.md) (17 shared connections)
- [ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List](ADR-023-_Package_Ownership_`game-`_vs_`services-`_vs_`npc-`_and_Fan-Out_Watch_List.md) (8 shared connections)
- [Room](Room.md) (7 shared connections)
- [SpellEffectType](SpellEffectType.md) (6 shared connections)
- [get_username_from_user](get_username_from_user.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (4 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (4 shared connections)
- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [security.ts](security.ts.md) (2 shared connections)
- [.publish_with_pool](publish_with_pool.md) (2 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/game/follow_service.py`
- `server/game/quest/quest_events.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_lifecycle_death.py`

## Audit Trail

- EXTRACTED: 243 (86%)
- INFERRED: 39 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*