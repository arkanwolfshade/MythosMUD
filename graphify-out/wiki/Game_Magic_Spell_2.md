# Game Magic Spell

> 6 nodes

## Key Concepts

- **.add_player_to_room()** (7 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (6 connections) — `server/game/movement_service.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_service.py`
- **Validate player and room IDs for add_player_to_room.** (1 connections) — `server/game/movement_service.py`
- **Update player current_room_id in persistence after room add.** (1 connections) — `server/game/movement_service.py`
- **Add a player to a room (for initial placement, teleportation, etc.).          Ar** (1 connections) — `server/game/movement_service.py`

## Relationships

- [Combat Client Crash Report](Combat_Client_Crash_Report.md) (3 shared connections)
- [Room Map Viewer UI](Room_Map_Viewer_UI.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 18 (90%)
- INFERRED: 2 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*