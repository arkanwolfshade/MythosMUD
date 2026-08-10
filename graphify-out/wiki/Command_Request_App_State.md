# Command Request App State

> 6 nodes

## Key Concepts

- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (6 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **Load fresh player from persistence for posture check when available.** (1 connections) — `server/game/movement_service.py`
- **Validate rooms, membership, and exit for movement.** (1 connections) — `server/game/movement_service.py`
- **Validate that a movement operation is allowed.          Args:             player** (1 connections) — `server/game/movement_service.py`

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (5 shared connections)
- [Combat Client Crash Report](Combat_Client_Crash_Report.md) (4 shared connections)
- [Room Map Viewer UI](Room_Map_Viewer_UI.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*