# Community 467

> 38 nodes

## Key Concepts

- **GameStateProvider** (30 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (14 connections)
- **.send_initial_game_state()** (13 connections) — `server/realtime/integration/game_state_provider.py`
- **Any** (13 connections)
- **.connection_manager()** (9 connections) — `server/game/magic/spell_effects.py`
- **._get_player_data_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **.convert_room_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_fallback_player_data()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- **._add_grace_period_indicators()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_following_for_client()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_room_data_with_conversion()** (5 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_players_batch()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.__init__()** (4 connections) — `server/realtime/integration/game_state_provider.py`
- **.get_npcs_batch()** (3 connections) — `server/realtime/integration/game_state_provider.py`
- **Connection manager for login grace period checks.** (1 connections) — `server/game/magic/spell_effects.py`
- **Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Get player name and add grace period indicators if applicable.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert player UUIDs to names in room_data.** (1 connections) — `server/realtime/integration/game_state_provider.py`
- **Convert player UUIDs and NPC IDs in room_data to names. CRITICAL: NEVER send…** (1 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 13 more nodes in this community*

## Relationships

- [Community 817](Community_817.md) (4 shared connections)
- [Community 200](Community_200.md) (4 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (4 shared connections)
- [Community 376](Community_376.md) (3 shared connections)
- [Community 42](Community_42.md) (2 shared connections)
- [Community 164](Community_164.md) (2 shared connections)
- [Community 326](Community_326.md) (2 shared connections)
- [Community 533](Community_533.md) (1 shared connections)
- [Community 68](Community_68.md) (1 shared connections)
- [Community 180](Community_180.md) (1 shared connections)
- [Community 888](Community_888.md) (1 shared connections)
- [Community 90](Community_90.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/realtime/integration/game_state_provider.py`

## Audit Trail

- EXTRACTED: 91 (90%)
- INFERRED: 10 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*