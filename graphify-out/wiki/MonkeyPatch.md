# MonkeyPatch

> 9 nodes

## Key Concepts

- **datetime** (9 connections)
- **._filter_active_players()** (8 connections) — `server/services/passive_lucidity_flux/service.py`
- **._is_player_active()** (6 connections) — `server/services/passive_lucidity_flux/service.py`
- **._normalize_datetime_timezone()** (5 connections) — `server/services/passive_lucidity_flux/service.py`
- **._parse_last_active()** (4 connections) — `server/services/passive_lucidity_flux/service.py`
- **Parse last_active from various formats.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Normalize datetime to timezone-aware UTC.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Check if player is active based on last_active and created_at.** (1 connections) — `server/services/passive_lucidity_flux/service.py`
- **Filter players to only those active in the last 5 minutes.** (1 connections) — `server/services/passive_lucidity_flux/service.py`

## Relationships

- [config](config.md) (7 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (3 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [EventDict](EventDict.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/service.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*