# test rate limiter utils

> 8 nodes

## Key Concepts

- **._resolve_context()** (9 connections) — `server/services/passive_lucidity_flux/service.py`
- **Player** (8 connections)
- **._get_room_for_context()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._count_companion_tiers()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._companion_modifier()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **Fetch room for context resolution. Returns None if persistence unavailable or fe** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Resolve context synchronously (legacy path).** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Count lucid companions and whether any destabilizing companion is present. Retur** (1 connections) — `server/services/passive_lucidity_flux/service.py`

## Relationships

- [config](config.md) (6 shared connections)
- [EventDict](EventDict.md) (4 shared connections)
- [MonkeyPatch](MonkeyPatch.md) (3 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [real time](real_time.md) (1 shared connections)
- [Test broadcast combat ended broadcasts](Test_broadcast_combat_ended_broadcasts.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 35 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*