# player room event

> 60 nodes

## Key Concepts

- **test_quest_events.py** (16 connections) — `server/tests/unit/game/test_quest_events.py`
- **quest_events.py** (15 connections) — `server/game/quest/quest_events.py`
- **subscribe_quest_events()** (15 connections) — `server/game/quest/quest_events.py`
- **test_lifespan_event_subscriptions.py** (15 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **subscribe_quest_events()** (13 connections) — `server/app/lifespan_event_subscriptions.py`
- **QuestCompleted** (13 connections) — `server/events/event_types.py`
- **lifespan_event_subscriptions.py** (12 connections) — `server/app/lifespan_event_subscriptions.py`
- **subscribe_room_occupants_refresh()** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **_make_on_player_entered()** (7 connections) — `server/game/quest/quest_events.py`
- **_make_on_npc_died()** (6 connections) — `server/game/quest/quest_events.py`
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **_make_on_player_left()** (5 connections) — `server/game/quest/quest_events.py`
- **test_quest_log_updated_event_envelope_shape()** (5 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **_entity_id_for_quest_offer()** (4 connections) — `server/game/quest/quest_events.py`
- **Any** (4 connections)
- **_parse_player_id()** (4 connections) — `server/game/quest/quest_events.py`
- **test_player_entered_starts_quest_by_room_trigger()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_entered_invalid_player_id_skips()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_player_left_records_exit_activity()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_records_kill_for_player_killer()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_npc_died_no_killer_skips()** (4 connections) — `server/tests/unit/game/test_quest_events.py`
- **test_subscribe_room_occupants_refresh_broadcasts_on_event()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_room_occupants_refresh_no_running_loop_returns_silently()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- **test_quest_completed_invalid_player_id_logs_warning()** (3 connections) — `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- *... and 35 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (19 shared connections)
- [party service game](party_service_game.md) (9 shared connections)
- [profession models rationale](profession_models_rationale.md) (4 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [quest game service](quest_game_service.md) (3 shared connections)
- [combat messaging services](combat_messaging_services.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)
- [command models moderation](command_models_moderation.md) (2 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (2 shared connections)
- [aggro threat services](aggro_threat_services.md) (2 shared connections)
- [lucidity event services](lucidity_event_services.md) (2 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (2 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/tests/unit/app/test_lifespan_event_subscriptions.py`
- `server/tests/unit/game/test_quest_events.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 229 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*