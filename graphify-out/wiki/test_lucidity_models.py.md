# test_lucidity_models.py

> 84 nodes

## Key Concepts

- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityExposureState** (23 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (21 connections) — `server/models/lucidity.py`
- **LucidityRepository** (14 connections) — `server/services/lucidity_repository.py`
- **lucidity_repository.py** (11 connections) — `server/services/lucidity_repository.py`
- **UUID** (9 connections)
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.delete_cooldowns_by_action_code_pattern()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **_utc_now()** (5 connections) — `server/services/lucidity_repository.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **Base** (4 connections)
- **test_lucidity_adjustment_log_creation()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_default_metadata()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_negative_delta()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_positive_delta()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_repr()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_lucidity_adjustment_log_with_location()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- *... and 59 more nodes in this community*

## Relationships

- [log_and_raise](log_and_raise.md) (25 shared connections)
- [LucidityService](LucidityService.md) (24 shared connections)
- [.get_instance](get_instance.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [PostgresCursor](PostgresCursor.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_repository.py`
- `server/tests/unit/models/test_lucidity_models.py`

## Audit Trail

- EXTRACTED: 154 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*