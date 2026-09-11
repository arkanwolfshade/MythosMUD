# LucidityTierCache

> 28 nodes

## Key Concepts

- **LucidityTierCache** (14 connections) — `server/services/lucidity_tier_cache.py`
- **test_lucidity_tier_cache.py** (9 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **lucidity_tier_cache.py** (8 connections) — `server/services/lucidity_tier_cache.py`
- **UUID** (5 connections)
- **.get_tier()** (4 connections) — `server/services/lucidity_tier_cache.py`
- **.is_deranged()** (4 connections) — `server/services/lucidity_tier_cache.py`
- **.clear()** (3 connections) — `server/services/lucidity_tier_cache.py`
- **.set_tier()** (3 connections) — `server/services/lucidity_tier_cache.py`
- **test_clear_removes_the_cached_tier()** (3 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **test_get_tier_is_none_for_unrecorded_player()** (3 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **test_is_deranged_false_for_other_tiers()** (3 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **test_is_deranged_false_on_cache_miss()** (3 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **test_set_tier_accepts_str_or_uuid_for_the_same_player()** (3 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **test_set_tier_then_is_deranged()** (3 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **.__init__()** (1 connections) — `server/services/lucidity_tier_cache.py`
- **In-memory cache of each player's current lucidity tier (#714). Exit…** (1 connections) — `server/services/lucidity_tier_cache.py`
- **Module-level singleton (mirrors phantom_hostile_service) -- callers MUST share…** (1 connections) — `server/services/lucidity_tier_cache.py`
- **Record this player's current tier.** (1 connections) — `server/services/lucidity_tier_cache.py`
- **Return the cached tier, or None if this player has never been recorded.** (1 connections) — `server/services/lucidity_tier_cache.py`
- **True only if the cached tier is exactly 'deranged' -- a cache miss is never…** (1 connections) — `server/services/lucidity_tier_cache.py`
- **Drop a player's cached tier (e.g. on disconnect).** (1 connections) — `server/services/lucidity_tier_cache.py`
- **Unit tests for the in-memory lucidity tier cache (#714). This cache is exit…** (1 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **A player never written to the cache has no recorded tier.** (1 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **Fail safe: an unrecorded player is never treated as deranged.** (1 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- **Only an exact 'deranged' tier makes is_deranged True.** (1 connections) — `server/tests/unit/services/test_lucidity_tier_cache.py`
- *... and 3 more nodes in this community*

## Relationships

- [test_look_room.py](test_look_room.py.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [room_update_event_builder.py](room_update_event_builder.py.md) (1 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (1 shared connections)

## Source Files

- `server/services/lucidity_tier_cache.py`
- `server/tests/unit/services/test_lucidity_tier_cache.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*