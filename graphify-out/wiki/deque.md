# deque

> 48 nodes · cohesion 0.06

## Key Concepts

- **NATSMessageHandler** (36 connections) — `server/realtime/nats_message_handler.py`
- **test_chat_segments.py** (34 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- **test_chat_event_category.py** (20 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **test_fake_npc_whisper_and_real_whisper_get_the_same_category()** (10 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **test_build_chat_event_tags_category_per_channel()** (8 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **_event()** (7 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- **_CapturingNats** (6 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **_chat_event_data()** (6 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **test_build_chat_event_unknown_channel_has_no_category()** (5 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **test_send_room_name_message_is_tagged_room_name()** (5 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **_apply()** (4 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- **test_chat_message_and_payload_carry_the_two_inputs_only_when_set()** (4 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- **.start()** (3 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **_nats_payload()** (3 connections) — `server/tests/unit/realtime/test_chat_event_category.py`
- **asyncio** (2 connections)
- **_payload()** (2 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- **ChatMessage** (2 connections)
- **test_a_player_speaker_event_has_no_segments()** (2 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- **test_a_receiver_copy_loses_stale_spans_when_nothing_is_styled_any_more()** (2 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- **test_an_npc_speaker_event_carries_the_styled_name()** (2 connections) — `server/tests/unit/realtime/test_chat_segments.py`
- *... and 23 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (17 shared connections)
- [test_database_helpers.py](test_database_helpers.py.md) (10 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (6 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [test_skill_service_graded.py](test_skill_service_graded.py.md) (4 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [_handle_admin_hallucinate_command](_handle_admin_hallucinate_command.md) (2 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (2 shared connections)
- [main](main.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_chat_event_category.py`
- `server/tests/unit/realtime/test_chat_segments.py`

## Audit Trail

- EXTRACTED: 118 (87%)
- INFERRED: 17 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*