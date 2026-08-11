# Test Refactoring Status

> 22 nodes

## Key Concepts

- **lucidity_repository.py** (11 connections) — `server/services/lucidity_repository.py`
- **UUID** (9 connections)
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **.delete_cooldowns_by_action_code_pattern()** (6 connections) — `server/services/lucidity_repository.py`
- **_utc_now()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **datetime** (3 connections)
- **Repository layer for lucidity-related persistence.** (1 connections) — `server/services/lucidity_repository.py`
- **Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE.** (1 connections) — `server/services/lucidity_repository.py`
- **Get player lucidity record.** (1 connections) — `server/services/lucidity_repository.py`
- **Get existing player lucidity record or create a new one.** (1 connections) — `server/services/lucidity_repository.py`
- **Add a lucidity adjustment log entry.** (1 connections) — `server/services/lucidity_repository.py`
- **Get exposure state for a player and entity archetype.** (1 connections) — `server/services/lucidity_repository.py`
- **Increment exposure state for a player and entity archetype.** (1 connections) — `server/services/lucidity_repository.py`
- **Get cooldown state for a player and action.** (1 connections) — `server/services/lucidity_repository.py`
- **Set or update cooldown for a player and action.** (1 connections) — `server/services/lucidity_repository.py`
- **Delete all cooldowns for a player matching an action code pattern.** (1 connections) — `server/services/lucidity_repository.py`

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (10 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (9 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (3 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (1 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (1 shared connections)
- [Postgres Adapter Infrastructure](Postgres_Adapter_Infrastructure.md) (1 shared connections)

## Source Files

- `server/services/lucidity_repository.py`

## Audit Trail

- EXTRACTED: 78 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*