# CorruptionTier

> 22 nodes

## Key Concepts

- **CorruptionTier** (42 connections) — `server/models/corruption.py`
- **test_corruption_reactions.py** (22 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **corruption_tier_cache.py** (12 connections) — `server/services/corruption_tier_cache.py`
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
- **StrEnum** (1 connections)
- **Corruption bands over 0..100. `PURE` is reserved for exactly 0 (#815) --…** (1 connections) — `server/models/corruption.py`
- **Threat multiplier from the corruption gap between an NPC and a player,…** (1 connections) — `server/npc/corruption_reactions.py`
- **In-memory cache of each player's previous corruption tier (#804). Unlike…** (1 connections) — `server/services/corruption_tier_cache.py`
- **Unit tests for NPC <-> player corruption relationship (#815 PR-4). Covers both…** (1 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **#815: the permanent scar (touched) stays private -- no special greeting for it.** (1 connections) — `server/tests/unit/npc/test_corruption_reactions.py`

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [format_occupant_display_name](format_occupant_display_name.md) (10 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (6 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [CorruptionService](CorruptionService.md) (5 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [test_passive_corruption_flux_service.py](test_passive_corruption_flux_service.py.md) (3 shared connections)
- [test_look_player.py](test_look_player.py.md) (2 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (2 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (2 shared connections)
- [CorruptionTierCache](CorruptionTierCache.md) (2 shared connections)
- [look_helpers.py](look_helpers.py.md) (1 shared connections)

## Source Files

- `server/models/corruption.py`
- `server/npc/corruption_reactions.py`
- `server/services/corruption_tier_cache.py`
- `server/tests/unit/npc/test_corruption_reactions.py`

## Audit Trail

- EXTRACTED: 72 (75%)
- INFERRED: 24 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*