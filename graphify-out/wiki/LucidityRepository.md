# LucidityRepository

> 28 nodes

## Key Concepts

- **LucidityRepository** (14 connections) — `server/services/lucidity_repository.py`
- **UUID** (9 connections)
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.delete_cooldowns_by_action_code_pattern()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **_utc_now()** (5 connections) — `server/services/lucidity_repository.py`
- **.delete()** (4 connections) — `server/caching/lru_cache.py`
- **.rowcount()** (4 connections) — `server/postgres_adapter.py`
- **datetime** (3 connections)
- **.__init__()** (2 connections) — `server/services/lucidity_repository.py`
- **AsyncSession** (1 connections)
- **Delete an item from the cache. Args: key: The key to delete Returns: True if…** (1 connections) — `server/caching/lru_cache.py`
- **Get the number of rows affected.** (1 connections) — `server/postgres_adapter.py`
- **Set or update cooldown for a player and action.** (1 connections) — `server/services/lucidity_repository.py`
- **Delete all cooldowns for a player matching an action code pattern.** (1 connections) — `server/services/lucidity_repository.py`
- **Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE.** (1 connections) — `server/services/lucidity_repository.py`
- **Data-access helpers for lucidity persistence.** (1 connections) — `server/services/lucidity_repository.py`
- **Get player lucidity record.** (1 connections) — `server/services/lucidity_repository.py`
- **Get existing player lucidity record or create a new one.** (1 connections) — `server/services/lucidity_repository.py`
- **Add a lucidity adjustment log entry.** (1 connections) — `server/services/lucidity_repository.py`
- *... and 3 more nodes in this community*

## Relationships

- [Player](Player.md) (11 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [K](K.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [PostgresCursor](PostgresCursor.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)

## Source Files

- `server/caching/lru_cache.py`
- `server/postgres_adapter.py`
- `server/services/lucidity_repository.py`

## Audit Trail

- EXTRACTED: 90 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*