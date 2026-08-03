# follow service game

> 36 nodes

## Key Concepts

- **test_look_npc_helpers.py** (34 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_from_dict()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_from_json_string()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_invalid_json()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_other_type()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_core_attributes()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info_no_lifecycle_state()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_from_current_room_id()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_from_current_room()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_get_npc_room_id_none()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Get the room ID from an NPC instance, checking both current_room and current_roo** (1 connections) — `server/commands/look_npc.py`
- **Test getting NPC room ID from current_room_id.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID from current_room when current_room_id is None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test getting NPC room ID when both are None.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Unit tests for look_npc helper functions.  Tests the helper functions in look_np** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_npc_stats_dict() handles dict input.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_npc_stats_dict() parses JSON string.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- *... and 11 more nodes in this community*

## Relationships

- [npc look commands](npc_look_commands.md) (21 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (6 shared connections)
- [rate limiter rationale](rate_limiter_rationale.md) (4 shared connections)
- [models player related](models_player_related.md) (4 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (2 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 114 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*