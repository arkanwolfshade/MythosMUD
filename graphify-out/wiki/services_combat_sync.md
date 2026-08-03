# services combat sync

> 78 nodes

## Key Concepts

- **.get_instance()** (35 connections) — `server/container/main.py`
- **EventPublisher** (23 connections) — `server/realtime/event_publisher.py`
- **quest_events.py** (14 connections) — `server/game/quest/quest_events.py`
- **subscribe_quest_events()** (13 connections) — `server/game/quest/quest_events.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **CombatDPSync** (11 connections) — `server/services/combat_hp_sync.py`
- **test_event_publisher_helpers.py** (9 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **._process_wander_action()** (8 connections) — `server/npc/threading.py`
- **._persist_player_dp_sync()** (8 connections) — `server/services/combat_hp_sync.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **Any** (6 connections)
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **_make_on_player_entered()** (5 connections) — `server/game/quest/quest_events.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **Any** (4 connections)
- **_make_on_player_left()** (4 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (4 connections) — `server/game/quest/quest_events.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- *... and 53 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (29 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [health models rationale](health_models_rationale.md) (5 shared connections)
- [event publisher realtime](event_publisher_realtime.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [services npc startup](services_npc_startup.md) (3 shared connections)
- [services user manager](services_user_manager.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (2 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/main.py`
- `server/game/quest/quest_events.py`
- `server/npc/npc_base.py`
- `server/npc/threading.py`
- `server/realtime/connection_manager.py`
- `server/realtime/event_publisher.py`
- `server/services/combat_hp_sync.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 269 (93%)
- INFERRED: 20 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*