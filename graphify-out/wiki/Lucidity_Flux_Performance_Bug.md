# Lucidity Flux Performance Bug

> 14 nodes

## Key Concepts

- **test_visual_indicator.py** (13 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_filter_other_players_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_filter_other_players_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_format_player_look_display_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_format_player_look_display_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_adds_linkdead_indicator()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **test_player_occupant_processor_no_linkdead_when_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Unit tests for visual indicator (linkdead) display.  Tests that "(linkdead)" ind** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test _filter_other_players() adds (linkdead) indicator for grace period players.** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test _filter_other_players() does not add (linkdead) when player not in grace pe** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test _format_player_look_display() adds (linkdead) indicator for grace period pl** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test _format_player_look_display() does not add (linkdead) when player not in gr** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test PlayerOccupantProcessor adds (linkdead) indicator for grace period players.** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`
- **Test PlayerOccupantProcessor does not add (linkdead) when player not in grace pe** (1 connections) — `server/tests/unit/realtime/test_visual_indicator.py`

## Relationships

- [Look Player Command](Look_Player_Command.md) (4 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (4 shared connections)
- [API Type Guards](API_Type_Guards.md) (4 shared connections)

## Source Files

- `server/tests/unit/realtime/test_visual_indicator.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*