# follow game service

> 152 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **EventHandler** (34 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **test_event_handlers_combat.py** (22 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **user_manager.py** (20 connections) — `server/services/user_manager.py`
- **NATSMessageHandlerMixinBase** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **_EventBusPublishPort** (7 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (7 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **test_nats_message_handler_base.py** (6 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_participant_key_strings()** (5 connections) — `server/realtime/event_handlers.py`
- *... and 127 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (31 shared connections)
- [Error Conversion](Error_Conversion.md) (29 shared connections)
- [command commands handler](command_commands_handler.md) (14 shared connections)
- [game chat service](game_chat_service.md) (13 shared connections)
- [character creation service](character_creation_service.md) (11 shared connections)
- [Room Broadcast](Room_Broadcast.md) (10 shared connections)
- [persistence combat services](persistence_combat_services.md) (10 shared connections)
- [services user manager](services_user_manager.md) (8 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (8 shared connections)
- [commands communication say](commands_communication_say.md) (6 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (6 shared connections)
- [occupant realtime formatter](occupant_realtime_formatter.md) (5 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/services/user_manager.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`

## Audit Trail

- EXTRACTED: 596 (93%)
- INFERRED: 48 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*