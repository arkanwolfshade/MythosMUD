# MessageFilteringHelper

> 35 nodes

## Key Concepts

- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **Any** (4 connections)
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver()** (3 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **.collect_room_targets()** (2 connections) — `server/realtime/message_filtering.py`
- **.preload_receiver_mute_data()** (2 connections) — `server/realtime/message_filtering.py`
- **Extract information from chat event. Args: chat_event: Chat event dictionary…** (1 connections) — `server/realtime/message_filtering.py`
- **Determine if mute check should be applied for a channel. Args: channel: Channel…** (1 connections) — `server/realtime/message_filtering.py`
- **Compare two room IDs using canonical room ID resolution. Args: player_room_id:…** (1 connections) — `server/realtime/message_filtering.py`
- **Get player's current room ID from online players cache. Args: player_id: Player…** (1 connections) — `server/realtime/message_filtering.py`
- **Get player's current room ID from async persistence layer. Args: player_id:…** (1 connections) — `server/realtime/message_filtering.py`
- **Helper class for message filtering operations.** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a player is currently in the specified room. Args: player_id: Player…** (1 connections) — `server/realtime/message_filtering.py`
- *... and 10 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (2 shared connections)
- [test_message_filtering_helpers.py](test_message_filtering_helpers.py.md) (2 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (2 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (1 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)
- [EventHandler](EventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_broadcast.py`

## Audit Trail

- EXTRACTED: 55 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*