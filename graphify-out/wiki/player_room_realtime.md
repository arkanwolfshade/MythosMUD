# player room realtime

> 134 nodes

## Key Concepts

- **lucidity.py** (34 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **LucidityExposureState** (26 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (25 connections) — `server/models/lucidity.py`
- **LucidityAdjustmentLog** (23 connections) — `server/models/lucidity.py`
- **test_lucidity_repository.py** (22 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **lucidity_repository.py** (12 connections) — `server/services/lucidity_repository.py`
- **UUID** (9 connections)
- **_utc_now()** (8 connections) — `server/models/lucidity.py`
- **LucidityActionCode** (8 connections) — `server/models/lucidity.py`
- **_utc_now()** (7 connections) — `server/services/lucidity_repository.py`
- **test_lucidity_utils.py** (7 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **.delete_cooldowns_by_action_code_pattern()** (5 connections) — `server/services/lucidity_repository.py`
- **Base** (4 connections)
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- *... and 109 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (30 shared connections)
- [combat models rationale](combat_models_rationale.md) (9 shared connections)
- [combat services persistence](combat_services_persistence.md) (6 shared connections)
- [world models rationale](world_models_rationale.md) (6 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (6 shared connections)
- [task registry app](task_registry_app.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (3 shared connections)
- [command helpers functions](command_helpers_functions.md) (2 shared connections)
- [services service phantom](services_service_phantom.md) (2 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (2 shared connections)
- [rescue service services](rescue_service_services.md) (2 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_repository.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/models/test_lucidity_utils.py`
- `server/tests/unit/services/test_lucidity_repository.py`

## Audit Trail

- EXTRACTED: 463 (94%)
- INFERRED: 28 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*