# _PostureConnectionManager

> 10 nodes

## Key Concepts

- **_PostureConnectionManager** (7 connections) — `server/realtime/posture_notify.py`
- **_send_personal_posture_message()** (5 connections) — `server/realtime/posture_notify.py`
- **_broadcast_room_posture_change()** (4 connections) — `server/realtime/posture_notify.py`
- **UUID** (4 connections)
- **.send_personal_message()** (3 connections) — `server/realtime/posture_notify.py`
- **.broadcast_to_room()** (2 connections) — `server/realtime/posture_notify.py`
- **Protocol** (1 connections)
- **Connection manager surface for posture fan-out.** (1 connections) — `server/realtime/posture_notify.py`
- **Send event to occupants of room_id.** (1 connections) — `server/realtime/posture_notify.py`
- **Send a personal WebSocket event to one player.** (1 connections) — `server/realtime/posture_notify.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [emit_posture_change](emit_posture_change.md) (3 shared connections)
- [build_event](build_event.md) (2 shared connections)

## Source Files

- `server/realtime/posture_notify.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*