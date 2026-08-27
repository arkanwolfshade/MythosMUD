# GameTerminal.tsx

> 85 nodes

## Key Concepts

- **quest_commands.py** (40 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (21 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **handle_quest_command()** (20 connections) — `server/commands/quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (14 connections) — `server/commands/quest_commands.py`
- **asyncio** (13 connections)
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **npc_definition_id()** (7 connections) — `server/commands/quest_commands.py`
- **emit_quest_npc_say()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_emit_npc_lines_for_results()** (6 connections) — `server/commands/quest_commands.py`
- **_quest_command_ready()** (6 connections) — `server/commands/quest_commands.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **quest_ask_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **quest_turnin_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **test_quest_ask_npc_not_in_room()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_success()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_npc_not_in_room()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_success()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **UUID** (6 connections)
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- *... and 60 more nodes in this community*

## Relationships

- [Communities (355 total, 223 thin omitted)](Communities_355_total,_223_thin_omitted.md) (11 shared connections)
- [Stats](Stats.md) (9 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (7 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [apply_communication_dampening](apply_communication_dampening.md) (2 shared connections)
- [Reporter](Reporter.md) (1 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/commands/test_quest_commands.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 202 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*