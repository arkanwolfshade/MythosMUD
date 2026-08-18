# server realtime occupant display

> 8 nodes

## Key Concepts

- **occupant_display.py** (11 connections) — `server/realtime/occupant_display.py`
- **format_occupant_display_name()** (10 connections) — `server/realtime/occupant_display.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **UUID** (4 connections)
- **_parse_occupant_player_id()** (3 connections) — `server/realtime/occupant_display.py`
- **Any** (2 connections)
- **Shared occupant display names for look text and Occupants panel events.** (1 connections) — `server/realtime/occupant_display.py`
- **Format an in-room player's Occupants/look name. Always list; grace badges only.** (1 connections) — `server/realtime/occupant_display.py`

## Relationships

- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (3 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (3 shared connections)
- [server commands look room](server_commands_look_room.md) (3 shared connections)
- [attributeerror](attributeerror.md) (3 shared connections)

## Source Files

- `server/realtime/occupant_display.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*