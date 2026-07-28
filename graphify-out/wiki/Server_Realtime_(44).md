# Server Realtime (44)

> 46 nodes

## Key Concepts

- **.state()** (35 connections) — `server/realtime/connection_state_machine.py`
- **GameStateProvider** (27 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (15 connections)
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (8 connections) — `server/realtime/nats_message_handler.py`
- **._convert_player_uuids_to_names()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
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

- [Server Realtime (8)](Server_Realtime_%288%29.md) (6 shared connections)
- [Server Npc](Server_Npc.md) (3 shared connections)
- [Server Npc (8)](Server_Npc_%288%29.md) (3 shared connections)
- [Server Realtime (17)](Server_Realtime_%2817%29.md) (3 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (3 shared connections)
- [Server Api (9)](Server_Api_%289%29.md) (2 shared connections)
- [Server Commands (6)](Server_Commands_%286%29.md) (2 shared connections)
- [Server Commands (10)](Server_Commands_%2810%29.md) (2 shared connections)
- [Server Commands (25)](Server_Commands_%2825%29.md) (2 shared connections)
- [Server Realtime (10)](Server_Realtime_%2810%29.md) (2 shared connections)
- [Server Realtime (21)](Server_Realtime_%2821%29.md) (2 shared connections)
- [Server Realtime (39)](Server_Realtime_%2839%29.md) (2 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 194 (81%)
- INFERRED: 46 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*