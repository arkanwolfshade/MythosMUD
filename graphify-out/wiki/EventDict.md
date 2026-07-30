# EventDict

> 12 nodes

## Key Concepts

- **._resolve_context_async()** (10 connections) — `server/services/passive_lucidity_flux/service.py`
- **Any** (8 connections)
- **._get_room_cached()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_base_flux_for_room()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **build_override_key()** (5 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **._build_room_cache()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._lookup_world_override_flux()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **Build override key from plane/zone/subzone hierarchy.** (1 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **Build room cache for all players.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Get room from cache or fetch from database with TTL management.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Look up base_flux and profile_source from room overrides. Returns (base_flux, pr** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Resolve environmental context for passive flux evaluation using cached room.** (1 connections) — `server/services/passive_lucidity_flux/service.py`

## Relationships

- [config](config.md) (9 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (4 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [rate overrides](rate_overrides.md) (2 shared connections)
- [Test broadcast combat ended broadcasts](Test_broadcast_combat_ended_broadcasts.md) (2 shared connections)
- [real time](real_time.md) (1 shared connections)
- [MonkeyPatch](MonkeyPatch.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/rate_overrides.py`
- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 49 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*