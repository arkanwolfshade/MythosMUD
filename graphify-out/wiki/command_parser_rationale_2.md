# command parser rationale

> 118 nodes

## Key Concepts

- **NPCDied** (35 connections) — `server/events/event_types.py`
- **test_lifecycle_manager.py** (27 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **lifecycle_death.py** (24 connections) — `server/npc/lifecycle_death.py`
- **NPCLifecycleRecord** (19 connections) — `server/npc/lifecycle_types.py`
- **_make_manager()** (18 connections) — `server/tests/unit/npc/test_lifecycle_manager.py`
- **RoomOccupantsRefreshRequested** (17 connections) — `server/events/event_types.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **test_quest_events.py** (16 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_lifecycle_death.py** (16 connections) — `server/tests/unit/npc/test_lifecycle_death.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **test_lifespan_event_subscriptions.py** (15 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **handle_npc_died_impl()** (11 connections) — `server/npc/lifecycle_death.py`
- **_mark_despawned_and_queue_respawn()** (9 connections) — `server/npc/lifecycle_death.py`
- **_remove_active_npc_and_notify()** (8 connections) — `server/npc/lifecycle_death.py`
- **_make_on_player_entered()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (6 connections) — `server/game/quest/quest_events.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **_make_on_player_left()** (5 connections) — `server/game/quest/quest_events.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **test_quest_log_updated_event_envelope_shape()** (5 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- *... and 93 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (64 shared connections)
- [models npc rationale](models_npc_rationale.md) (24 shared connections)
- [quest game service](quest_game_service.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [command service commands](command_service_commands.md) (2 shared connections)
- [player realtime event](player_realtime_event.md) (2 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/npc/test_lifecycle_death.py`
- `server/tests/unit/npc/test_lifecycle_manager.py`

## Audit Trail

- EXTRACTED: 481 (91%)
- INFERRED: 48 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*