# Chat NATS Publisher

> 20 nodes

## Key Concepts

- **_format_npc_description()** (15 connections) — `server/commands/look_npc.py`
- **test_format_npc_description_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_description_fallback_long_description()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_description_fallback_short_description()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_description_fallback_desc()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_description_no_description()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_description_empty_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_description()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description_fallback()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description_no_description()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Format NPC description with fallback.** (1 connections) — `server/commands/look_npc.py`
- **Test formatting NPC description successfully.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test formatting NPC description with long_description fallback.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test formatting NPC description with short_description fallback.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test formatting NPC description with desc fallback.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test formatting NPC description when no description available.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test formatting NPC description when description is empty string.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test _format_npc_description() returns description from definition.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _format_npc_description() uses fallback when description is empty.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _format_npc_description() uses alternative attributes.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`

## Relationships

- [Look NPC Command](Look_NPC_Command.md) (7 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (4 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (3 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*