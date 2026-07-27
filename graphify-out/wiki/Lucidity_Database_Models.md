# Lucidity Database Models

> 73 nodes · cohesion 0.04

## Key Concepts

- **PlayerLucidity** (48 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (27 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **lucidity.py** (25 connections) — `server/models/lucidity.py`
- **LucidityAdjustmentLog** (25 connections) — `server/models/lucidity.py`
- **LucidityExposureState** (24 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (21 connections) — `server/models/lucidity.py`
- **AsyncSession** (11 connections) — `server/database_helpers.py`
- **lucidity_repository.py** (11 connections) — `server/services/lucidity_repository.py`
- **async_sessionmaker** (10 connections) — `server/database_helpers.py`
- **AsyncEngine** (10 connections) — `server/database_helpers.py`
- **Path** (10 connections) — `server/database_helpers.py`
- **get_session_maker()** (8 connections) — `server/database_helpers.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **Any** (5 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **test_get_session_maker()** (3 connections) — `server/tests/unit/infrastructure/test_database_helpers.py`
- **test_lucidity_adjustment_log_creation()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_default_metadata()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_negative_delta()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_positive_delta()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_repr()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_with_location()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_cooldown_creation()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_cooldown_different_action_codes()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- *... and 48 more nodes in this community*

## Relationships

- [[SQLAlchemy Model Base]] (25 shared connections)
- [[NPC Admin API]] (20 shared connections)
- [[Player Domain Model]] (14 shared connections)
- [[Lucidity Rescue Helpers]] (9 shared connections)
- [[Services Rescue Service]] (7 shared connections)
- [[Database Helper Tests]] (6 shared connections)
- [[Alias Expansion Logic]] (4 shared connections)
- [[Player Related Models]] (4 shared connections)
- [[Invite Registration Model]] (4 shared connections)
- [[API Test Fixtures]] (4 shared connections)
- [[Lucidity State Models]] (3 shared connections)
- [[Services Lucidity Repository]] (3 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/models/lucidity.py`
- `server/services/lucidity_repository.py`
- `server/tests/unit/infrastructure/test_database_helpers.py`
- `server/tests/unit/models/test_lucidity_models.py`

## Audit Trail

- EXTRACTED: 267 (77%)
- INFERRED: 80 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
