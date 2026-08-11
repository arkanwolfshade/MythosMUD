# Look Player Command

> 74 nodes

## Key Concepts

- **test_look_player.py** (32 connections) — `server/tests/unit/commands/test_look_player.py`
- **look_player.py** (26 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (22 connections) — `server/commands/look_player.py`
- **_get_lucidity_label()** (17 connections) — `server/commands/look_helpers.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **look_helpers.py** (16 connections) — `server/commands/look_helpers.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **_get_players_in_room()** (12 connections) — `server/commands/look_player.py`
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **_get_visible_equipment()** (11 connections) — `server/commands/look_helpers.py`
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **Any** (8 connections)
- **_apply_grace_period_labels()** (6 connections) — `server/commands/look_player.py`
- **Any** (4 connections)
- **_player_id_uuid()** (4 connections) — `server/commands/look_player.py`
- **UUID** (3 connections)
- **test_get_players_in_room_success()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_empty()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_invalid_uuid()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_non_iterable()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_find_matching_players_success()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_find_matching_players_no_match()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_select_target_player_single_match()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_select_target_player_no_matches()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_select_target_player_with_instance_number()** (3 connections) — `server/tests/unit/commands/test_look_player.py`
- *... and 49 more nodes in this community*

## Relationships

- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (28 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (11 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Lucidity Flux Performance Bug](Lucidity_Flux_Performance_Bug.md) (4 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (3 shared connections)
- [API Type Guards](API_Type_Guards.md) (3 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (2 shared connections)
- [Server Process Termination](Server_Process_Termination.md) (1 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_player.py`

## Audit Trail

- EXTRACTED: 314 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*