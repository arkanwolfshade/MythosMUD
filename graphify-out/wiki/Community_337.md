# Community 337

> 50 nodes

## Key Concepts

- **CorruptionTier** (29 connections) — `server/models/corruption.py`
- **test_corruption_reactions.py** (22 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **format_occupant_display_name()** (20 connections) — `server/realtime/occupant_display.py`
- **test_occupant_display.py** (16 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **occupant_display.py** (14 connections) — `server/realtime/occupant_display.py`
- **corruption_tier_cache.py** (12 connections) — `server/services/corruption_tier_cache.py`
- **_reset_cache()** (9 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **corruption_hostility_scale()** (7 connections) — `server/npc/corruption_reactions.py`
- **_pick_greeting()** (7 connections) — `server/npc/corruption_reactions.py`
- **_reset_cache()** (7 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **_no_grace_patches()** (7 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_compute_tier_boundaries()** (6 connections) — `server/tests/unit/models/test_corruption.py`
- **test_format_occupant_display_name_no_badge_when_touched()** (6 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_apply_grace_badges()** (5 connections) — `server/realtime/occupant_display.py`
- **test_build_corruption_aware_greeting_fires_on_entry_to_the_npcs_room()** (5 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_uses_normal_greeting_for_touched_player()** (5 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_format_occupant_display_name_badge_defiled()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_from_marked()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_warped()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_no_connection_manager_returns_name_unchanged()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **UUID** (5 connections)
- **_apply_corruption_badge()** (4 connections) — `server/realtime/occupant_display.py`
- **test_pick_greeting_boundary_at_npc_tainted_threshold()** (4 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_recoils_from_marked_player_when_npc_is_untainted()** (4 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_uses_normal_greeting_for_pure_player()** (4 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- *... and 25 more nodes in this community*

## Relationships

- [Game Event Types](Game_Event_Types.md) (11 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (8 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Community 87](Community_87.md) (3 shared connections)
- [Community 170](Community_170.md) (3 shared connections)
- [Community 124](Community_124.md) (2 shared connections)
- [Community 139](Community_139.md) (2 shared connections)
- [Community 1170](Community_1170.md) (2 shared connections)
- [Community 68](Community_68.md) (1 shared connections)
- [Community 46](Community_46.md) (1 shared connections)
- [Community 43](Community_43.md) (1 shared connections)
- [Community 579](Community_579.md) (1 shared connections)

## Source Files

- `server/models/corruption.py`
- `server/npc/corruption_reactions.py`
- `server/realtime/occupant_display.py`
- `server/services/corruption_tier_cache.py`
- `server/tests/unit/models/test_corruption.py`
- `server/tests/unit/npc/test_corruption_reactions.py`
- `server/tests/unit/realtime/test_occupant_display.py`

## Audit Trail

- EXTRACTED: 136 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*