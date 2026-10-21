# WebSocketManager

> 53 nodes · cohesion 0.05

## Key Concepts

- **MessageFilteringHelper** (31 connections) — `server/realtime/message_filtering.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **._should_include_target()** (6 connections) — `server/realtime/message_filtering.py`
- **._debug_dump_receiver_mute_cache()** (5 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (5 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (4 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **message_filtering_helper()** (4 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **._room_id_from_player_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **Any** (3 connections)
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.collect_room_targets()** (2 connections) — `server/realtime/message_filtering.py`
- **UUID** (2 connections)
- **fixture** (2 connections)
- **test_compare_canonical_rooms()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **test_extract_chat_event_info()** (2 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 28 more nodes in this community*

## Relationships

- [Room](Room.md) (6 shared connections)
- [mp_regeneration_service](mp_regeneration_service.md) (4 shared connections)
- [_handle_admin_hallucinate_command](_handle_admin_hallucinate_command.md) (1 shared connections)
- [Chat Panel](Chat_Panel.md) (1 shared connections)
- [Chaosium CoC Catalog](Chaosium_CoC_Catalog.md) (1 shared connections)
- [analyze_markdownlint.py](analyze_markdownlint.py.md) (1 shared connections)
- [schemas/__init__.py](schemas-__init__.py.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [skills_commands.py](skills_commands.py.md) (1 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (1 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 77 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*