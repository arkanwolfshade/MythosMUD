# commands quest rationale

> 75 nodes

## Key Concepts

- **quest_commands.py** (39 connections) — `server/commands/quest_commands.py`
- **handle_quest_command()** (20 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (14 connections) — `server/commands/quest_commands.py`
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **npc_definition_id()** (7 connections) — `server/commands/quest_commands.py`
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **UUID** (6 connections)
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_emit_npc_lines_for_results()** (6 connections) — `server/commands/quest_commands.py`
- **_quest_command_ready()** (6 connections) — `server/commands/quest_commands.py`
- **_get_container_and_persistence()** (5 connections) — `server/commands/quest_commands.py`
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- **_format_quest_log()** (5 connections) — `server/commands/quest_commands.py`
- **_handle_quest_abandon()** (5 connections) — `server/commands/quest_commands.py`
- **ExitStack** (5 connections)
- **test_quest_ask_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_npc_not_in_room()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_npc_not_in_room()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- *... and 50 more nodes in this community*

## Relationships

- [quest chat game](quest_chat_game.md) (9 shared connections)
- [commands communication flows](commands_communication_flows.md) (5 shared connections)
- [commands position system](commands_position_system.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [services service hallucination](services_service_hallucination.md) (3 shared connections)
- [quest game service](quest_game_service.md) (3 shared connections)
- [cache caching lru](cache_caching_lru.md) (2 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (2 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (2 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/tests/unit/commands/test_quest_commands.py`

## Audit Trail

- EXTRACTED: 310 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*