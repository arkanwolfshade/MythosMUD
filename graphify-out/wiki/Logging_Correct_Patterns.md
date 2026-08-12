# Logging Correct Patterns

> 94 nodes

## Key Concepts

- **lucidity.py** (33 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityAdjustmentLog** (23 connections) — `server/models/lucidity.py`
- **LucidityExposureState** (23 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **LucidityRepository** (14 connections) — `server/services/lucidity_repository.py`
- **lucidity_repository.py** (11 connections) — `server/services/lucidity_repository.py`
- **UUID** (9 connections)
- **_utc_now()** (8 connections) — `server/models/lucidity.py`
- **LucidityActionCode** (8 connections) — `server/models/lucidity.py`
- **test_lucidity_utils.py** (7 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **.delete_cooldowns_by_action_code_pattern()** (6 connections) — `server/services/lucidity_repository.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **_utc_now()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_or_create_player_lucidity()** (5 connections) — `server/services/lucidity_repository.py`
- **.add_adjustment_log()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_exposure_state()** (5 connections) — `server/services/lucidity_repository.py`
- **.get_cooldown()** (5 connections) — `server/services/lucidity_repository.py`
- **Base** (4 connections)
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **Any** (3 connections)
- *... and 69 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (19 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (13 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (10 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (10 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (6 shared connections)
- [Mythos Calendar Time Service](Mythos_Calendar_Time_Service.md) (4 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (3 shared connections)
- [Character Selection Screens](Character_Selection_Screens.md) (3 shared connections)
- [Game Client Container](Game_Client_Container.md) (2 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (1 shared connections)
- [Redis to NATS Migration](Redis_to_NATS_Migration.md) (1 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_repository.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/models/test_lucidity_utils.py`

## Audit Trail

- EXTRACTED: 342 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*