# CorruptionTier

> 66 nodes

## Key Concepts

- **CorruptionTier** (42 connections) — `server/models/corruption.py`
- **corruption.py** (26 connections) — `server/models/corruption.py`
- **test_corruption_reactions.py** (22 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **format_occupant_display_name()** (20 connections) — `server/realtime/occupant_display.py`
- **compute_tier()** (17 connections) — `server/models/corruption.py`
- **occupant_display.py** (16 connections) — `server/realtime/occupant_display.py`
- **test_occupant_display.py** (16 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **corruption_reactions.py** (13 connections) — `server/npc/corruption_reactions.py`
- **corruption_tier_cache.py** (12 connections) — `server/services/corruption_tier_cache.py`
- **build_corruption_aware_greeting()** (10 connections) — `server/npc/corruption_reactions.py`
- **corruption_hostility_scale()** (9 connections) — `server/npc/corruption_reactions.py`
- **_reset_cache()** (9 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_pick_greeting()** (7 connections) — `server/npc/corruption_reactions.py`
- **_reset_cache()** (7 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **_no_grace_patches()** (7 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_corruption.py** (7 connections) — `server/tests/unit/models/test_corruption.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **test_compute_tier_boundaries()** (6 connections) — `server/tests/unit/models/test_corruption.py`
- **test_format_occupant_display_name_no_badge_when_touched()** (6 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_build_corruption_aware_greeting_fires_on_entry_to_the_npcs_room()** (5 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_pick_greeting_uses_normal_greeting_for_touched_player()** (5 connections) — `server/tests/unit/npc/test_corruption_reactions.py`
- **test_format_occupant_display_name_badge_defiled()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_from_marked()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_warped()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_no_connection_manager_returns_name_unchanged()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- *... and 41 more nodes in this community*

## Relationships

- [player_presence_tracker.py](player_presence_tracker.py.md) (9 shared connections)
- [CorruptionService](CorruptionService.md) (6 shared connections)
- [look_helpers.py](look_helpers.py.md) (5 shared connections)
- [server/models/__init__.py](server-models-__init__.py.md) (5 shared connections)
- [corruption_service.py](corruption_service.py.md) (5 shared connections)
- [NPCBase](NPCBase.md) (5 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (5 shared connections)
- [passive_corruption_flux/service.py](passive_corruption_flux-service.py.md) (4 shared connections)
- [test_passive_corruption_flux_service.py](test_passive_corruption_flux_service.py.md) (4 shared connections)
- [CorruptionRepository](CorruptionRepository.md) (4 shared connections)
- [test_look_player.py](test_look_player.py.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)

## Source Files

- `server/models/corruption.py`
- `server/npc/corruption_reactions.py`
- `server/realtime/occupant_display.py`
- `server/services/corruption_tier_cache.py`
- `server/tests/unit/models/test_corruption.py`
- `server/tests/unit/npc/test_corruption_reactions.py`
- `server/tests/unit/realtime/test_occupant_display.py`

## Audit Trail

- EXTRACTED: 201 (89%)
- INFERRED: 24 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*