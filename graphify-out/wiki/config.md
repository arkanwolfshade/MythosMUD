# config

> 17 nodes

## Key Concepts

- **PassiveLucidityFluxService** (34 connections) — `server/services/passive_lucidity_flux/service.py`
- **.process_tick()** (14 connections) — `server/services/passive_lucidity_flux/service.py`
- **._process_single_player()** (12 connections) — `server/services/passive_lucidity_flux/service.py`
- **._load_players()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **AsyncSession** (4 connections)
- **._load_lucidity_records()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **passive_lucidity_flux_service.py** (3 connections) — `server/services/passive_lucidity_flux_service.py`
- **._should_process_tick()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_adaptive_resistance()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._apply_residual()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._prune_trackers()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **._emit_telemetry()** (2 connections) — `server/services/passive_lucidity_flux/service.py`
- **Applies passive LCD flux each in-game minute with structured telemetry.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Process a single player's passive flux.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Evaluate passive LCD flux for the current tick.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Load players from database.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Backward-compatible re-export of passive lucidity flux service.** (1 connections) — `server/services/passive_lucidity_flux_service.py`

## Relationships

- [EventDict](EventDict.md) (9 shared connections)
- [MonkeyPatch](MonkeyPatch.md) (7 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (6 shared connections)
- [Test broadcast combat ended broadcasts](Test_broadcast_combat_ended_broadcasts.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [ConnectionsComponent](ConnectionsComponent.md) (1 shared connections)
- [. is npc in combat()](_is_npc_in_combat%28%29.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [Lock](Lock.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`
- `server/services/passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 84 (91%)
- INFERRED: 8 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*