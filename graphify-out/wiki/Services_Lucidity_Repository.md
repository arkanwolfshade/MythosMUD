# Services Lucidity Repository

> 24 nodes · cohesion 0.11

## Key Concepts

- **UUID** (9 connections) — `server/services/lucidity_repository.py`
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **_utc_now()** (5 connections) — `server/services/lucidity_repository.py`
- **.delete_cooldowns_by_action_code_pattern()** (4 connections) — `server/services/lucidity_repository.py`
- **datetime** (3 connections) — `server/services/lucidity_repository.py`
- **LucidityCooldown** (2 connections) — `server/services/lucidity_repository.py`
- **LucidityExposureState** (2 connections) — `server/services/lucidity_repository.py`
- **PlayerLucidity** (2 connections) — `server/services/lucidity_repository.py`
- **LucidityAdjustmentLog** (1 connections) — `server/services/lucidity_repository.py`
- **Set or update cooldown for a player and action.** (1 connections) — `server/services/lucidity_repository.py`
- **Delete all cooldowns for a player matching an action code pattern.** (1 connections) — `server/services/lucidity_repository.py`
- **Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE.** (1 connections) — `server/services/lucidity_repository.py`
- **Get player lucidity record.** (1 connections) — `server/services/lucidity_repository.py`
- **Get existing player lucidity record or create a new one.** (1 connections) — `server/services/lucidity_repository.py`
- **Add a lucidity adjustment log entry.** (1 connections) — `server/services/lucidity_repository.py`
- **Get exposure state for a player and entity archetype.** (1 connections) — `server/services/lucidity_repository.py`
- **Increment exposure state for a player and entity archetype.** (1 connections) — `server/services/lucidity_repository.py`
- **Get cooldown state for a player and action.** (1 connections) — `server/services/lucidity_repository.py`

## Relationships

- [[Lucidity State Models]] (8 shared connections)
- [[Lucidity Database Models]] (3 shared connections)
- [[LRU Cache Manager]] (1 shared connections)

## Source Files

- `server/services/lucidity_repository.py`

## Audit Trail

- EXTRACTED: 73 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
