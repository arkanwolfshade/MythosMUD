# Player Command Developer Guide

> 18 nodes

## Key Concepts

- **AsciiMapRenderer** (52 connections) — `server/services/ascii_map_renderer.py`
- **TestVerticalExitCharBetween** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_bidirectional_returns_pipe()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_south_returns_v()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_returns_caret()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_no_exit_returns_none()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_uses_caret_bidirectional_uses_pipe()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_and_one_way_south_assign_caret_and_v_by_target()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.__init__()** (2 connections) — `server/services/ascii_map_renderer.py`
- **Renders ASCII maps from room coordinate data.      Supports multiple map styles** (1 connections) — `server/services/ascii_map_renderer.py`
- **Initialize the ASCII map renderer.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Tests for _vertical_exit_char_between (|, v, ^).** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **Bidirectional vertical exit renders as a vertical bar.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way south exit renders as a lowercase 'v'.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way north exit renders as a caret.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **When there are no vertical exits, the helper returns None.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way North-only exit renders ^; bidirectional vertical exit renders |.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **One-way north renders ^ and one-way south renders v; symbols match direction to** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Relationships

- [ASCII Map Renderer](ASCII_Map_Renderer.md) (11 shared connections)
- [Cursor Plans Pydantic](Cursor_Plans_Pydantic.md) (8 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (5 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (5 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (5 shared connections)
- [Contexts Themecontext Hooks](Contexts_Themecontext_Hooks.md) (4 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (3 shared connections)
- [Command Processor](Command_Processor.md) (2 shared connections)
- [Command Commands Validation](Command_Commands_Validation.md) (1 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`
- `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Audit Trail

- EXTRACTED: 83 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*