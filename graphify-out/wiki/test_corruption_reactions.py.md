# test_corruption_reactions.py

> 17 nodes

## Key Concepts

- **test_corruption_reactions.py** (22 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **corruption_hostility_scale()** (9 connections) — `server/npc/corruption_reactions.py`
- **_pick_greeting()** (7 connections) — `server/npc/corruption_reactions.py`
- **_reset_cache()** (7 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_build_corruption_aware_greeting_fires_on_entry_to_the_npcs_room()** (5 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_uses_normal_greeting_for_touched_player()** (5 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_boundary_at_npc_tainted_threshold()** (4 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_recoils_from_marked_player_when_npc_is_untainted()** (4 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_uses_normal_greeting_for_pure_player()** (4 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_welcomes_marked_player_from_tainted_npc()** (4 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_corruption_hostility_scale_intermediate_gap()** (2 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_corruption_hostility_scale_neutral_when_either_side_missing()** (2 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_corruption_hostility_scale_sharpens_with_gap()** (2 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_corruption_hostility_scale_softens_when_identical()** (2 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **Threat multiplier from the corruption gap between an NPC and a player,…** (1 connections) — `server/npc/corruption_reactions.py`
- **Unit tests for NPC <-> player corruption relationship (#815 PR-4). Covers both…** (1 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **#815: the permanent scar (touched) stays private -- no special greeting for it.** (1 connections) — `server/tests/unit/npc/test_corruption_reactions.py`

## Relationships

- [event_types.py](event_types.py.md) (9 shared connections)
- [CorruptionTier](CorruptionTier.md) (8 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/npc/corruption_reactions.py`
- `server/tests/unit/npc/test_corruption_reactions.py`

## Audit Trail

- EXTRACTED: 45 (88%)
- INFERRED: 6 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*