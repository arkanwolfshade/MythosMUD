# command parser()

> 16 nodes

## Key Concepts

- **OccupantFormatter** (37 connections) — `server/realtime/occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_empty()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_add_valid_name_to_lists()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_player_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_npc()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_dict_players()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Formats and separates occupants by type.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Initialize occupant formatter.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Test OccupantFormatter._is_valid_name_for_occupant() returns False for empty str** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_player_name_for_update() skips UUID player name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_dict_occupant_for_update() processes NPC dict.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() separates dict players.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`

## Relationships

- [occupant formatter](occupant_formatter.md) (15 shared connections)
- [. add valid name to](_add_valid_name_to.md) (6 shared connections)
- [Test load room cache async](Test_load_room_cache_async.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [metadata](metadata.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [Test process combined rows processes](Test_process_combined_rows_processes.md) (1 shared connections)
- [Test query rooms with exits](Test_query_rooms_with_exits.md) (1 shared connections)
- [Test process exits for room](Test_process_exits_for_room.md) (1 shared connections)
- [Test warmup room cache calls](Test_warmup_room_cache_calls.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*