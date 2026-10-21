# FeatureFlagService

> 103 nodes · cohesion 0.03

## Key Concepts

- **test_look_player.py** (37 connections) — `server/tests/unit/commands/test_look_player.py`
- **look_player.py** (30 connections) — `server/commands/look_player.py`
- **_format_player_look_display()** (26 connections) — `server/commands/look_player.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **_get_players_in_room()** (13 connections) — `server/commands/look_player.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **asyncio** (13 connections)
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **test_look_player_helpers.py** (12 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **Any** (10 connections)
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **_apply_grace_period_labels()** (6 connections) — `server/commands/look_player.py`
- **_normalize_room_player_ids()** (4 connections) — `server/commands/look_player.py`
- **_player_id_uuid()** (4 connections) — `server/commands/look_player.py`
- **_resolve_room_player()** (4 connections) — `server/commands/look_player.py`
- **test_find_matching_players_no_match()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_find_matching_players_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_format_player_look_display_marked_or_worse_adds_prose()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_empty()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_invalid_uuid()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_non_iterable()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_get_players_in_room_success()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_multiple_matches()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_handle_player_look_not_found()** (4 connections) — `server/tests/unit/commands/test_look_player.py`
- *... and 78 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (12 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (7 shared connections)
- [ChatLogger](ChatLogger.md) (6 shared connections)
- [_RecordingRoom](_RecordingRoom.md) (5 shared connections)
- [ResourceManager](ResourceManager.md) (4 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (3 shared connections)
- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)

## Source Files

- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 222 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*