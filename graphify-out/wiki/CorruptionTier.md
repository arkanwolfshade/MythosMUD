# CorruptionTier

> 41 nodes

## Key Concepts

- **CorruptionTier** (42 connections) — `server/models/corruption.py`
- **format_occupant_display_name()** (20 connections) — `server/realtime/occupant_display.py`
- **compute_tier()** (17 connections) — `server/models/corruption.py`
- **occupant_display.py** (16 connections) — `server/realtime/occupant_display.py`
- **test_occupant_display.py** (16 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **corruption_tier_cache.py** (12 connections) — `server/services/corruption_tier_cache.py`
- **_reset_cache()** (9 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_no_grace_patches()** (7 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_corruption.py** (7 connections) — `server/tests/unit/models/test_corruption.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **test_compute_tier_boundaries()** (6 connections) — `server/tests/unit/models/test_corruption.py`
- **test_format_occupant_display_name_no_badge_when_touched()** (6 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_defiled()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_from_marked()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_warped()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_no_connection_manager_returns_name_unchanged()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **UUID** (5 connections)
- **_apply_corruption_badge()** (4 connections) — `server/realtime/occupant_display.py`
- **test_compute_tier_corrupted_floor_matches_is_corrupted()** (4 connections) — `server/tests/unit/models/test_corruption.py`
- **test_compute_tier_pure_is_reserved_for_exactly_zero()** (4 connections) — `server/tests/unit/models/test_corruption.py`
- **test_format_occupant_display_name_combines_grace_and_corruption_badges()** (4 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_no_badge_when_pure()** (4 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_unparseable_player_id_returns_name_unchanged()** (4 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_parse_occupant_player_id()** (3 connections) — `server/realtime/occupant_display.py`
- **Any** (2 connections)
- *... and 16 more nodes in this community*

## Relationships

- [Player](Player.md) (8 shared connections)
- [test_corruption_reactions.py](test_corruption_reactions.py.md) (8 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (6 shared connections)
- [CorruptionService](CorruptionService.md) (5 shared connections)
- [look_helpers.py](look_helpers.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [passive_corruption_flux/service.py](passive_corruption_flux-service.py.md) (3 shared connections)
- [test_passive_corruption_flux_service.py](test_passive_corruption_flux_service.py.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)

## Source Files

- `server/models/corruption.py`
- `server/realtime/occupant_display.py`
- `server/services/corruption_tier_cache.py`
- `server/tests/unit/models/test_corruption.py`
- `server/tests/unit/realtime/test_occupant_display.py`

## Audit Trail

- EXTRACTED: 123 (84%)
- INFERRED: 24 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*