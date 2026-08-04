# message filtering realtime

> 120 nodes

## Key Concepts

- **NATSError** (105 connections) — `server/services/nats_exceptions.py`
- **test_message_filtering.py** (36 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.is_player_in_room()** (7 connections) — `server/realtime/message_filtering.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **Any** (4 connections)
- **.is_player_muted_by_receiver()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **.start()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.preload_receiver_mute_data()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- *... and 95 more nodes in this community*

## Relationships

- [nats exceptions services](nats_exceptions_services.md) (20 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (16 shared connections)
- [nats message handler](nats_message_handler.md) (9 shared connections)
- [commands communication say](commands_communication_say.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [nats services service](nats_services_service.md) (7 shared connections)
- [services combat sync](services_combat_sync.md) (7 shared connections)
- [subzone realtime nats](subzone_realtime_nats.md) (7 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [combat validator validators](combat_validator_validators.md) (4 shared connections)
- [startup npc services](startup_npc_services.md) (4 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (3 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 334 (84%)
- INFERRED: 63 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*