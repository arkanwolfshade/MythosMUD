# realtime message filtering

> 23 nodes

## Key Concepts

- **.is_player_in_room()** (7 connections) — `server/realtime/message_filtering.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **Any** (4 connections)
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Initialize message filtering helper.          Args:             connection_manag** (1 connections) — `server/realtime/message_filtering.py`
- **Extract information from chat event.          Args:             chat_event: Chat** (1 connections) — `server/realtime/message_filtering.py`
- **Determine if mute check should be applied for a channel.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Compare two room IDs using canonical room ID resolution.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Get player's current room ID from online players cache.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Get player's current room ID from async persistence layer.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a player is currently in the specified room.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a receiving player has muted the sender using a provided UserManager in** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a player has muted the sender.          Args:             user_manager:** (1 connections) — `server/realtime/message_filtering.py`
- **Filter target players based on room location and mute status.          Args:** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a receiving player has muted the sender.** (1 connections) — `server/realtime/nats_message_handler_broadcast.py`

## Relationships

- [circuit breaker realtime](circuit_breaker_realtime.md) (10 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (2 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler_broadcast.py`

## Audit Trail

- EXTRACTED: 55 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*