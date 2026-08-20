# NATSMessageHandler

> 49 nodes

## Key Concepts

- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **realtime/conftest.py** (24 connections) — `server/tests/unit/realtime/conftest.py`
- **fixture** (15 connections)
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **player_room_event_handler()** (5 connections) — `server/tests/unit/realtime/conftest.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **mock_utils()** (4 connections) — `server/tests/unit/realtime/conftest.py`
- **nats_message_handler()** (4 connections) — `server/tests/unit/realtime/conftest.py`
- **.start()** (3 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **mock_chat_logger()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_logger()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_message_builder()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_name_extractor()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_occupant_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_room_sync_service()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_subject_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_user_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_websocket()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_ws_connection_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- *... and 24 more nodes in this community*

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (8 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (2 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (2 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (1 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 87 (90%)
- INFERRED: 10 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*