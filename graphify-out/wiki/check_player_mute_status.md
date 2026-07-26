# .check_player_mute_status

> 11 nodes · cohesion 0.18

## Key Concepts

- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **Any** (4 connections)
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler.py`
- **Extract information from chat event.          Args:             chat_event: Chat** (1 connections) — `server/realtime/message_filtering.py`
- **Initialize message filtering helper.          Args:             connection_manag** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a receiving player has muted the sender using a provided UserManager in** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a player has muted the sender.          Args:             user_manager:** (1 connections) — `server/realtime/message_filtering.py`
- **Check if a receiving player has muted the sender.** (1 connections) — `server/realtime/nats_message_handler.py`

## Relationships

- [MessageFilteringHelper](MessageFilteringHelper.md) (6 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 25 (89%)
- INFERRED: 3 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*