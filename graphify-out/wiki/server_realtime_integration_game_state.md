# server realtime integration game state

> 43 nodes

## Key Concepts

- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (14 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (8 connections) — `server/realtime/nats_message_handler.py`
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
- **_not_configured_async()** (3 connections) — `server/realtime/nats_message_handler.py`
- **Any** (2 connections)
- **setter** (1 connections)
- **Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 18 more nodes in this community*

## Relationships

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (3 shared connections)
- [server tests unit realtime integration](server_tests_unit_realtime_integration.md) (2 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (2 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (2 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (2 shared connections)
- [server realtime connection initialization initialize](server_realtime_connection_initialization_initialize.md) (1 shared connections)
- [server realtime integration init](server_realtime_integration_init.md) (1 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 98 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*