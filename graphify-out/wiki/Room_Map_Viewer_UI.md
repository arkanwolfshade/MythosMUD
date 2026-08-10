# Room Map Viewer UI

> 19 nodes

## Key Concepts

- **UUID** (18 connections)
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (8 connections) — `server/game/movement_service.py`
- **.move_player()** (8 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (5 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **Room** (2 connections)
- **Exception** (1 connections)
- **Validate movement parameters. Returns False if validation fails (same room), rai** (1 connections) — `server/game/movement_service.py`
- **Get and validate rooms for movement.** (1 connections) — `server/game/movement_service.py`
- **Execute the atomic room transfer.** (1 connections) — `server/game/movement_service.py`
- **Mark destination room as explored (non-blocking).** (1 connections) — `server/game/movement_service.py`
- **Handle movement errors with monitoring.** (1 connections) — `server/game/movement_service.py`
- **Run movement logic while holding the service lock.** (1 connections) — `server/game/movement_service.py`
- **Log movement timing breakdown after a successful move.** (1 connections) — `server/game/movement_service.py`
- **Move a player from one room to another atomically.          This operation ensur** (1 connections) — `server/game/movement_service.py`

## Relationships

- [Combat Client Crash Report](Combat_Client_Crash_Report.md) (14 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (6 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (3 shared connections)
- [Command Request App State](Command_Request_App_State.md) (3 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [Claude Agents Deps](Claude_Agents_Deps.md) (2 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 81 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*