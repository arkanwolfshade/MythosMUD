# .state()

> 46 nodes

## Key Concepts

- **.state()** (35 connections) — `server/realtime/connection_state_machine.py`
- **GameStateProvider** (24 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (15 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.get_player()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (5 connections)
- **.get_room_occupants()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **_not_configured_async()** (3 connections) — `server/realtime/nats_message_handler.py`
- **Any** (2 connections)
- *... and 21 more nodes in this community*

## Relationships

- [Any](Any.md) (6 shared connections)
- [login grace period](login_grace_period.md) (5 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [websocket handler commands](websocket_handler_commands.md) (3 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [disconnect grace period](disconnect_grace_period.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [communication commands support](communication_commands_support.md) (2 shared connections)
- [rescue commands](rescue_commands.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (2 shared connections)
- [test game state provider](test_game_state_provider.md) (2 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 191 (81%)
- INFERRED: 45 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*