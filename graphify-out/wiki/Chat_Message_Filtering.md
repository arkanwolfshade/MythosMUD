# Chat Message Filtering

> 49 nodes

## Key Concepts

- **MessageFilteringHelper** (23 connections) — `server/realtime/message_filtering.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.is_player_in_room()** (7 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **Any** (4 connections)
- **.is_player_muted_by_receiver()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler.py`
- **message_filtering_helper()** (3 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.collect_room_targets()** (2 connections) — `server/realtime/message_filtering.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_extract_chat_event_info()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_should_apply_mute_check()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_compare_canonical_rooms()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_get_player_room_from_online_players()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_get_player_room_from_online_players_not_found()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 24 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (4 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (2 shared connections)
- [Performance Optimization Summary](Performance_Optimization_Summary.md) (1 shared connections)
- [Dead Letter Queue](Dead_Letter_Queue.md) (1 shared connections)
- [Vim Editor Guidelines](Vim_Editor_Guidelines.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 130 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*