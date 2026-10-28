# PlayerRepositoryProtocol

> 71 nodes · cohesion 0.05

## Key Concepts

- **test_look_npc_helpers.py** (34 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **look_npc.py** (30 connections) — `server/commands/look_npc.py`
- **_parse_stat_datetime()** (16 connections) — `server/commands/look_npc.py`
- **_format_npc_description()** (15 connections) — `server/commands/look_npc.py`
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_should_include_npc()** (14 connections) — `server/commands/look_npc.py`
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (9 connections) — `server/commands/look_npc.py`
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_core_attributes()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info_no_lifecycle_state()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description_fallback()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description_no_description()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_from_dict()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- *... and 46 more nodes in this community*

## Relationships

- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (50 shared connections)
- [Commands](Commands.md) (6 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [command_parser.py](command_parser.py.md) (3 shared connections)
- [_RecordingRoom](_RecordingRoom.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [session](session.md) (1 shared connections)
- [look_container.py](look_container.py.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 197 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*