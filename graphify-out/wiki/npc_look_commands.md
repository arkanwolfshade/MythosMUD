# npc look commands

> 68 nodes

## Key Concepts

- **test_look_npc.py** (59 connections) — `server/tests/unit/commands/test_look_npc.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
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
- **test_format_lifecycle_info_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_lifecycle_info_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_no_match()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_no_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- *... and 43 more nodes in this community*

## Relationships

- [follow service game](follow_service_game.md) (21 shared connections)
- [rate limiter rationale](rate_limiter_rationale.md) (10 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (9 shared connections)
- [command parser rationale](command_parser_rationale.md) (7 shared connections)
- [models player related](models_player_related.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [look command commands](look_command_commands.md) (3 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)
- [admin shutdown commands](admin_shutdown_commands.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 292 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*