# message filtering realtime

> 89 nodes

## Key Concepts

- **NATSError** (105 connections) — `server/services/nats_exceptions.py`
- **test_message_filtering.py** (36 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.preload_receiver_mute_data()** (3 connections) — `server/realtime/message_filtering.py`
- **message_filtering_helper()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_start_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_partial_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_nats_error_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_message_filtering_helper_init()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets_empty()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_preload_receiver_mute_data()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_preload_receiver_mute_data_excludes_sender()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets_with_canonical_id()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- *... and 64 more nodes in this community*

## Relationships

- [circuit breaker realtime](circuit_breaker_realtime.md) (25 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (20 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (12 shared connections)
- [nats message handler](nats_message_handler.md) (9 shared connections)
- [subzone realtime nats](subzone_realtime_nats.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [spawn npc services](spawn_npc_services.md) (5 shared connections)
- [services combat sync](services_combat_sync.md) (4 shared connections)
- [message chat nats](message_chat_nats.md) (3 shared connections)
- [character creation validate](character_creation_validate.md) (2 shared connections)
- [services passive lucidity](services_passive_lucidity.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 233 (80%)
- INFERRED: 57 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*