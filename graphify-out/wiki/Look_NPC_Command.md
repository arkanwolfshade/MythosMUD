# Look NPC Command

> 152 nodes

## Key Concepts

- **test_look_npc.py** (59 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_look_npc_helpers.py** (34 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **_parse_stat_datetime()** (16 connections) — `server/commands/look_npc.py`
- **_format_npc_description()** (15 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (10 connections) — `server/commands/look_npc.py`
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_parse_npc_stats_dict_from_dict()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_from_json_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_invalid_json()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_non_dict_non_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_core_attributes_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_other_stats_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_other_stats_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- *... and 127 more nodes in this community*

## Relationships

- [NATS Connection State Machine](NATS_Connection_State_Machine.md) (10 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (7 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (4 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (1 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 536 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*