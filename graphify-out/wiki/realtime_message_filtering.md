# realtime message filtering

> 59 nodes

## Key Concepts

- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **EventHandler** (24 connections) — `server/realtime/event_handlers.py`
- **.is_player_in_room()** (7 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **_as_event_data_dict()** (6 connections) — `server/realtime/event_handlers.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **Any** (4 connections)
- **.is_player_muted_by_receiver()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **test_event_handlers_combat.py** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.preload_receiver_mute_data()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- *... and 34 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (9 shared connections)
- [Item Instances](Item_Instances.md) (4 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [instance game manager](instance_game_manager.md) (2 shared connections)
- [message nats handler](message_nats_handler.md) (2 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (2 shared connections)
- [message filtering helpers](message_filtering_helpers.md) (2 shared connections)
- [message formatters realtime](message_formatters_realtime.md) (1 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (1 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (1 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 170 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*