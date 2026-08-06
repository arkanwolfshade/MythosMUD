# commands quest rationale

> 110 nodes

## Key Concepts

- **test_look_npc.py** (59 connections) — `server/tests/unit/commands/test_look_npc.py`
- **quest_commands.py** (39 connections) — `server/commands/quest_commands.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **Any** (18 connections)
- **Any** (14 connections)
- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **_should_include_npc()** (14 connections) — `server/commands/look_npc.py`
- **handle_journal_command()** (14 connections) — `server/commands/quest_commands.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_format_single_npc_result()** (10 connections) — `server/commands/look_npc.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **npc_definition_id()** (7 connections) — `server/commands/quest_commands.py`
- **emit_quest_npc_say()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **UUID** (6 connections)
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_emit_npc_lines_for_results()** (6 connections) — `server/commands/quest_commands.py`
- *... and 85 more nodes in this community*

## Relationships

- [npc look commands](npc_look_commands.md) (45 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (11 shared connections)
- [map layout useMapLayout](map_layout_useMapLayout.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [game chat moderation](game_chat_moderation.md) (6 shared connections)
- [quest chat game](quest_chat_game.md) (6 shared connections)
- [dialogue service game](dialogue_service_game.md) (5 shared connections)
- [connection realtime statistics](connection_realtime_statistics.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [look helpers commands](look_helpers_commands.md) (3 shared connections)
- [quest game service](quest_game_service.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (2 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/commands/quest_commands.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 495 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*