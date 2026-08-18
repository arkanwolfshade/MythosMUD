# server realtime integration game state

> 39 nodes

## Key Concepts

- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (14 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **Game state provision for connection management. This module provides…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get player name and add grace period indicators if applicable.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert player UUIDs to names in room_data.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 14 more nodes in this community*

## Relationships

- [server realtime integration game state](server_realtime_integration_game_state.md) (9 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [deque](deque.md) (3 shared connections)
- [server tests unit realtime integration](server_tests_unit_realtime_integration.md) (3 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (3 shared connections)
- [server container main get container](server_container_main_get_container.md) (3 shared connections)
- [server realtime integration init](server_realtime_integration_init.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (2 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (1 shared connections)
- [server realtime room subscription manager](server_realtime_room_subscription_manager.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`

## Audit Trail

- EXTRACTED: 111 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*