# AliasStorage

> 9 nodes

## Key Concepts

- **player_position_service.py** (9 connections) — `server/services/player_position_service.py`
- **SupportsPlayerPersistence** (6 connections) — `server/services/player_position_service.py`
- **SupportsConnectionManager** (5 connections) — `server/services/player_position_service.py`
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **AliasStorage** (2 connections)
- **Protocol** (2 connections)
- **Player posture coordination service for MythosMUD.  As noted in the Pnakotic Man** (1 connections) — `server/services/player_position_service.py`
- **Persistence surface required for posture updates.** (1 connections) — `server/services/player_position_service.py`
- **Live presence surface used to mirror posture into online player records.** (1 connections) — `server/services/player_position_service.py`

## Relationships

- [. apply player info()](_apply_player_info%28%29.md) (4 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (3 shared connections)
- [go command](go_command.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (1 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*