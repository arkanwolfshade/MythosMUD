# PassiveCorruptionFluxService

> 29 nodes

## Key Concepts

- **PassiveCorruptionFluxService** (18 connections) — `server/services/passive_corruption_flux/service.py`
- **.process_tick_for_player()** (12 connections) — `server/services/passive_corruption_flux/service.py`
- **._resolve_context()** (10 connections) — `server/services/passive_corruption_flux/service.py`
- **._resolve_player_and_context()** (10 connections) — `server/services/passive_corruption_flux/service.py`
- **FluxRoom** (9 connections) — `server/services/passive_corruption_flux/service.py`
- **lookup_profile()** (7 connections) — `server/services/passive_lucidity_flux/config.py`
- **_as_str_attr()** (6 connections) — `server/services/passive_corruption_flux/service.py`
- **._lookup_db_override()** (6 connections) — `server/services/passive_corruption_flux/service.py`
- **._lookup_rate_for_room()** (5 connections) — `server/services/passive_corruption_flux/service.py`
- **._lookup_target_for_room()** (5 connections) — `server/services/passive_corruption_flux/service.py`
- **._bound_delta()** (4 connections) — `server/services/passive_corruption_flux/service.py`
- **._tier_floor()** (4 connections) — `server/services/passive_corruption_flux/service.py`
- **datetime** (4 connections)
- **._apply_residual()** (3 connections) — `server/services/passive_corruption_flux/service.py`
- **._get_room()** (3 connections) — `server/services/passive_corruption_flux/service.py`
- **._signed_flux_toward_target()** (3 connections) — `server/services/passive_corruption_flux/service.py`
- **UUID** (3 connections)
- **._should_process_tick()** (2 connections) — `server/services/passive_corruption_flux/service.py`
- **Player** (1 connections)
- **Protocol** (1 connections)
- **Fractional-to-integer bank, identical in shape to passive_lucidity_flux's -- a…** (1 connections) — `server/services/passive_corruption_flux/service.py`
- **Bottom of the player's CURRENT tier -- a purifying room cleanses within a tier…** (1 connections) — `server/services/passive_corruption_flux/service.py`
- **Direction is derived from current-vs-target; a room can't supply a fixed sign…** (1 connections) — `server/services/passive_corruption_flux/service.py`
- **Clamp the residual bank's raw delta to the room's ceiling (rising) or the…** (1 connections) — `server/services/passive_corruption_flux/service.py`
- **Load the player and their room, and resolve this tick's flux context. None on…** (1 connections) — `server/services/passive_corruption_flux/service.py`
- *... and 4 more nodes in this community*

## Relationships

- [passive_corruption_flux/service.py](passive_corruption_flux-service.py.md) (13 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (4 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (1 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)
- [CorruptionService](CorruptionService.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)

## Source Files

- `server/services/passive_corruption_flux/service.py`
- `server/services/passive_lucidity_flux/config.py`

## Audit Trail

- EXTRACTED: 66 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*