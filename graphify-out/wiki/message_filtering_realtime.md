# message filtering realtime

> 11 nodes

## Key Concepts

- **test_message_filtering.py** (36 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_error_returns_false()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence_no_layer()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence_mock_player()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_via_persistence()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_global_mute_and_admin()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_by_receiver_exception()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_with_user_manager_async_paths()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_check_player_mute_status_patched_and_emote()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_filter_target_players_room_and_mute()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Unit tests for message filtering.  Tests the MessageFilteringHelper class.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`

## Relationships

- [skill game service](skill_game_service.md) (6 shared connections)
- [game skill service](game_skill_service.md) (4 shared connections)
- [commands communication say](commands_communication_say.md) (3 shared connections)
- [game room service](game_room_service.md) (3 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (3 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (2 shared connections)
- [room game service](room_game_service.md) (2 shared connections)
- [room service game](room_service_game.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [infrastructure persistence core](infrastructure_persistence_core.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_filtering.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*