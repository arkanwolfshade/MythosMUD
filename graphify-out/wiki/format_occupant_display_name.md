# format_occupant_display_name

> 24 nodes

## Key Concepts

- **format_occupant_display_name()** (20 connections) — `server/realtime/occupant_display.py`
- **occupant_display.py** (16 connections) — `server/realtime/occupant_display.py`
- **test_occupant_display.py** (16 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_reset_cache()** (9 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_no_grace_patches()** (7 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **test_format_occupant_display_name_no_badge_when_touched()** (6 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_defiled()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_from_marked()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_badge_warped()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_no_connection_manager_returns_name_unchanged()** (5 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **UUID** (5 connections)
- **_apply_corruption_badge()** (4 connections) — `server/realtime/occupant_display.py`
- **test_format_occupant_display_name_combines_grace_and_corruption_badges()** (4 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_no_badge_when_pure()** (4 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **test_format_occupant_display_name_unparseable_player_id_returns_name_unchanged()** (4 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **_parse_occupant_player_id()** (3 connections) — `server/realtime/occupant_display.py`
- **Any** (2 connections)
- **Shared occupant display names for look text and Occupants panel events.** (1 connections) — `server/realtime/occupant_display.py`
- **Append a corruption badge for a `marked`-or-worse tier. Cache-only (#815's…** (1 connections) — `server/realtime/occupant_display.py`
- **Format an in-room player's Occupants/look name: grace badges plus a corruption…** (1 connections) — `server/realtime/occupant_display.py`
- **Unit tests for shared occupant display name formatting. Tests…** (1 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **#815: the permanent scar is deliberately invisible in the room -- only a…** (1 connections) — `server/tests/unit/realtime/test_occupant_display.py`
- **No connection_manager means no grace/corruption lookup is even attempted.** (1 connections) — `server/tests/unit/realtime/test_occupant_display.py`

## Relationships

- [CorruptionTier](CorruptionTier.md) (10 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_display.py`
- `server/tests/unit/realtime/test_occupant_display.py`

## Audit Trail

- EXTRACTED: 72 (92%)
- INFERRED: 6 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*