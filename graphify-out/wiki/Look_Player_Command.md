# Look Player Command

> 186 nodes

## Key Concepts

- **test_look_player.py** (32 connections) — `server/tests/unit/commands/test_look_player.py`
- **test_look_helpers.py** (30 connections) — `server/tests/unit/commands/test_look_helpers.py`
- **look_player.py** (26 connections) — `server/commands/look_player.py`
- **test_look_helpers_functions.py** (23 connections) — `server/tests/unit/commands/test_look_helpers_functions.py`
- **_format_player_look_display()** (22 connections) — `server/commands/look_player.py`
- **_get_health_label()** (17 connections) — `server/commands/look_helpers.py`
- **_get_lucidity_label()** (17 connections) — `server/commands/look_helpers.py`
- **_select_target_player()** (17 connections) — `server/commands/look_player.py`
- **look_helpers.py** (16 connections) — `server/commands/look_helpers.py`
- **_handle_player_look()** (13 connections) — `server/commands/look_player.py`
- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **_get_players_in_room()** (12 connections) — `server/commands/look_player.py`
- **_try_lookup_player_implicit()** (12 connections) — `server/commands/look_player.py`
- **test_look_player_helpers.py** (12 connections) — `server/tests/unit/commands/test_look_player_helpers.py`
- **_parse_instance_number()** (11 connections) — `server/commands/look_helpers.py`
- **_get_visible_equipment()** (11 connections) — `server/commands/look_helpers.py`
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
- **_get_wearable_container_service()** (9 connections) — `server/commands/look_helpers.py`
- **_find_matching_players()** (9 connections) — `server/commands/look_player.py`
- **Any** (8 connections)
- **_apply_grace_period_labels()** (6 connections) — `server/commands/look_player.py`
- **Any** (4 connections)
- **_player_id_uuid()** (4 connections) — `server/commands/look_player.py`
- **UUID** (3 connections)
- **test_parse_instance_number_hyphen_syntax()** (3 connections) — `server/tests/unit/commands/test_look_helpers.py`
- *... and 161 more nodes in this community*

## Relationships

- [Commands Command Look](Commands_Command_Look.md) (8 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (7 shared connections)
- [API Type Guards](API_Type_Guards.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (3 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [Schedule Service Loader](Schedule_Service_Loader.md) (2 shared connections)
- [Structured Concurrency Patterns](Structured_Concurrency_Patterns.md) (1 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/commands/look_player.py`
- `server/tests/unit/commands/test_look_helpers.py`
- `server/tests/unit/commands/test_look_helpers_functions.py`
- `server/tests/unit/commands/test_look_player.py`
- `server/tests/unit/commands/test_look_player_helpers.py`
- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 640 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*