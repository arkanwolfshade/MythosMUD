# Community 429

> 41 nodes

## Key Concepts

- **player_connection_setup.py** (24 connections) — `server/realtime/player_connection_setup.py`
- **handle_new_connection_setup()** (18 connections) — `server/realtime/player_connection_setup.py`
- **test_player_connection_setup.py** (17 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **_manager()** (11 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **asyncio** (11 connections)
- **_trigger_quests_for_room_on_spawn()** (9 connections) — `server/realtime/player_connection_setup.py`
- **_broadcast_player_entered_game()** (8 connections) — `server/realtime/player_connection_setup.py`
- **_update_player_last_active()** (8 connections) — `server/realtime/player_connection_setup.py`
- **_send_room_occupants_update_after_connection()** (7 connections) — `server/realtime/player_connection_setup.py`
- **UUID** (7 connections)
- **_add_player_to_room_silently()** (6 connections) — `server/realtime/player_connection_setup.py`
- **Any** (6 connections)
- **test_broadcast_player_entered_game_success_and_error()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_send_room_occupants_update_paths()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_update_player_last_active_database_error()** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_player_connection_setup_grace_period.py** (5 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **_stable_room_id_for_quest()** (4 connections) — `server/realtime/player_connection_setup.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_reconnection_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`
- **test_add_player_to_room_silently_paths()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_handle_new_connection_setup_ends_combat_on_login()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_handle_new_connection_setup_room_none_early_return()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_trigger_quests_no_service()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_trigger_quests_success_and_failure()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **test_update_player_last_active_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- *... and 16 more nodes in this community*

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (7 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Community 41](Community_41.md) (3 shared connections)
- [Community 43](Community_43.md) (3 shared connections)
- [Community 139](Community_139.md) (2 shared connections)
- [Community 329](Community_329.md) (1 shared connections)
- [Community 1271](Community_1271.md) (1 shared connections)
- [Community 46](Community_46.md) (1 shared connections)

## Source Files

- `server/realtime/player_connection_setup.py`
- `server/tests/unit/realtime/test_player_connection_setup.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 112 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*