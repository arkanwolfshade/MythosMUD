# mp_regeneration_service

> 7 nodes · cohesion 0.29

## Key Concepts

- **BroadcastFilterContext** (11 connections) — `server/realtime/message_filtering.py`
- **test_filter_target_players_includes_allowed_player()** (5 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_filter_target_players_skips_mute_check_for_non_sensitive_channel()** (5 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_filter_target_players_room_and_mute()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Per-broadcast constants threaded through target filtering (issue #787: was 8…** (1 connections) — `server/realtime/message_filtering.py`
- **A player who is in-room, unmuted, and not the sender is included in the result.…** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **A channel outside MUTE_SENSITIVE_CHANNELS bypasses the mute check entirely.…** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`

## Relationships

- [Chaosium CoC Catalog](Chaosium_CoC_Catalog.md) (4 shared connections)
- [WebSocketManager](WebSocketManager.md) (4 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Down_Darker_Trails__2026-08-12.md) (3 shared connections)
- [skills_commands.py](skills_commands.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering.py`

## Audit Trail

- EXTRACTED: 15 (71%)
- INFERRED: 6 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*