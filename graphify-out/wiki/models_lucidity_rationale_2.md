# models lucidity rationale

> 26 nodes

## Key Concepts

- **LucidityRepository** (14 connections) — `server/services/lucidity_repository.py`
- **lucidity_repository.py** (11 connections) — `server/services/lucidity_repository.py`
- **UUID** (9 connections)
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **_utc_now()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **.delete_cooldowns_by_action_code_pattern()** (5 connections) — `server/services/lucidity_repository.py`
- **datetime** (3 connections)
- **.__init__()** (2 connections) — `server/services/lucidity_repository.py`
- **AsyncSession** (1 connections)
- **Repository layer for lucidity-related persistence.** (1 connections) — `server/services/lucidity_repository.py`
- **Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE.** (1 connections) — `server/services/lucidity_repository.py`
- **Data-access helpers for lucidity persistence.** (1 connections) — `server/services/lucidity_repository.py`
- **Get player lucidity record.** (1 connections) — `server/services/lucidity_repository.py`
- **Get existing player lucidity record or create a new one.** (1 connections) — `server/services/lucidity_repository.py`
- **Add a lucidity adjustment log entry.** (1 connections) — `server/services/lucidity_repository.py`
- **Get exposure state for a player and entity archetype.** (1 connections) — `server/services/lucidity_repository.py`
- **Increment exposure state for a player and entity archetype.** (1 connections) — `server/services/lucidity_repository.py`
- **Get cooldown state for a player and action.** (1 connections) — `server/services/lucidity_repository.py`
- **Set or update cooldown for a player and action.** (1 connections) — `server/services/lucidity_repository.py`
- *... and 1 more nodes in this community*

## Relationships

- [world models rationale](world_models_rationale.md) (9 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (7 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (1 shared connections)
- [postgres adapter infrastructure](postgres_adapter_infrastructure.md) (1 shared connections)

## Source Files

- `server/services/lucidity_repository.py`

## Audit Trail

- EXTRACTED: 95 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*