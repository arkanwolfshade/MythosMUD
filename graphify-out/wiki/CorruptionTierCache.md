# CorruptionTierCache

> 11 nodes

## Key Concepts

- **CorruptionTierCache** (6 connections) — `server/services/corruption_tier_cache.py`
- **.get_tier()** (4 connections) — `server/services/corruption_tier_cache.py`
- **.set_tier()** (4 connections) — `server/services/corruption_tier_cache.py`
- **UUID** (4 connections)
- **.clear()** (3 connections) — `server/services/corruption_tier_cache.py`
- **CorruptionTier** (2 connections)
- **.__init__()** (1 connections) — `server/services/corruption_tier_cache.py`
- **Module-level singleton (mirrors `lucidity_tier_cache`) -- callers MUST share…** (1 connections) — `server/services/corruption_tier_cache.py`
- **Record this player's current tier.** (1 connections) — `server/services/corruption_tier_cache.py`
- **Return the cached tier, or `pure` if this player has never been recorded.** (1 connections) — `server/services/corruption_tier_cache.py`
- **Drop a player's cached tier (e.g. on disconnect).** (1 connections) — `server/services/corruption_tier_cache.py`

## Relationships

- [CorruptionTier](CorruptionTier.md) (2 shared connections)

## Source Files

- `server/services/corruption_tier_cache.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*