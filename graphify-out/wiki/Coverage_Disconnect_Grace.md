# Coverage Disconnect Grace

> 14 nodes

## Key Concepts

- **_should_include_npc()** (14 connections) — `server/commands/look_npc.py`
- **test_should_include_npc_alive_with_name()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_should_include_npc_dead()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_should_include_npc_no_name()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_should_include_npc()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_should_include_npc_no_name()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_should_include_npc_not_alive()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Check if an NPC should be included in the results (has name and is alive).** (1 connections) — `server/commands/look_npc.py`
- **Test should_include_npc for alive NPC with name.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test should_include_npc for dead NPC.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test should_include_npc for NPC without name.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test _should_include_npc() returns True for valid NPC.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _should_include_npc() returns False when no name.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _should_include_npc() returns False when not alive.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`

## Relationships

- [Look NPC Command](Look_NPC_Command.md) (7 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (4 shared connections)
- [Player GUID Formatter](Player_GUID_Formatter.md) (2 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*