# .validate player name field()

> 150 nodes

## Key Concepts

- **test_follow_service.py** (41 connections) — `server/tests/unit/game/test_follow_service.py`
- **.__post_init__()** (21 connections) — `server/events/event_types.py`
- **quest_events.py** (14 connections) — `server/game/quest/quest_events.py`
- **subscribe_quest_events()** (13 connections) — `server/game/quest/quest_events.py`
- **lifespan_event_subscriptions.py** (12 connections) — `server/app/lifespan_event_subscriptions.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **subscribe_quest_events()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (11 connections) — `server/events/event_types.py`
- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_lifespan_event_subscriptions.py** (8 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (7 connections) — `server/app/lifespan_event_subscriptions.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **_make_on_player_entered()** (5 connections) — `server/game/quest/quest_events.py`
- **._get_integration_dependencies()** (5 connections) — `server/npc/npc_base.py`
- **.move_to_room()** (5 connections) — `server/npc/npc_base.py`
- **test_quest_log_updated_event_envelope_shape()** (5 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **Any** (4 connections)
- **_make_on_player_left()** (4 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (4 connections) — `server/game/quest/quest_events.py`
- **test_follow_request_event_envelope_shape()** (4 connections) — `server/tests/unit/game/test_follow_service.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- *... and 125 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (48 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)
- [QuestCompleted](QuestCompleted.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [test party service](test_party_service.md) (2 shared connections)
- [test combat messaging integration](test_combat_messaging_integration.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)
- [notify quest abandoned()](notify_quest_abandoned%28%29.md) (1 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/game/test_follow_service.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 397 (95%)
- INFERRED: 22 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*