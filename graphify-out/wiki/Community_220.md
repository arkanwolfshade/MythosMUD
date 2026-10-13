# Community 220

> 69 nodes

## Key Concepts

- **GameStateProvider** (45 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (18 connections)
- **.send_initial_game_state()** (13 connections) — `server/realtime/integration/game_state_provider.py`
- **Any** (12 connections)
- **.connection_manager()** (10 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_data_for_client()** (9 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._apply_grace_period_suffixes()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._build_client_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_player()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **Player** (6 connections)
- **._get_login_grace_period_status()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_lucidity_for_client()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 44 more nodes in this community*

## Relationships

- [Community 185](Community_185.md) (9 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 760](Community_760.md) (4 shared connections)
- [Community 46](Community_46.md) (2 shared connections)
- [Community 139](Community_139.md) (2 shared connections)
- [Community 1179](Community_1179.md) (1 shared connections)
- [Community 344](Community_344.md) (1 shared connections)
- [Community 1393](Community_1393.md) (1 shared connections)
- [Community 207](Community_207.md) (1 shared connections)
- [Community 1175](Community_1175.md) (1 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (1 shared connections)
- [Community 523](Community_523.md) (1 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 137 (87%)
- INFERRED: 21 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*