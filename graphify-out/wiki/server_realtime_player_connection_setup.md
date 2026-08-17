# server realtime player connection setup

> 39 nodes

## Key Concepts

- **handle_new_connection_setup()** (19 connections) — `server/realtime/player_connection_setup.py`
- **test_player_connection_setup.py** (18 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **_trigger_quests_for_room_on_spawn()** (11 connections) — `server/realtime/player_connection_setup.py`
- **_manager()** (11 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **asyncio** (11 connections)
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (8 connections) — `server/realtime/player_connection_setup.py`
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_add_player_to_room_silently()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **test_player_connection_setup_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_broadcast_player_entered_game_success_and_error()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_send_room_occupants_update_paths()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_update_player_last_active_database_error()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **_stable_room_id_for_quest()** (4 connections) — `server/realtime/player_connection_setup.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_add_player_to_room_silently_paths()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_handle_new_connection_setup_ends_combat_on_login()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_handle_new_connection_setup_room_none_early_return()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_trigger_quests_no_service()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_trigger_quests_success_and_failure()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_update_player_last_active_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_update_player_last_active_success()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- *... and 14 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (4 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [server realtime player presence utils](server_realtime_player_presence_utils.md) (1 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (1 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (1 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (1 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (1 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/tests/unit/realtime/test_player_connection_setup.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 102 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*