# Lucidity & Rescue Service

> 205 nodes

## Key Concepts

- **PlayerLucidity** (69 connections) — `server/models/lucidity.py`
- **lucidity.py** (35 connections) — `server/models/lucidity.py`
- **test_rescue_service.py** (33 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **test_lucidity_repository.py** (25 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **LucidityExposureState** (23 connections) — `server/models/lucidity.py`
- **LucidityCooldown** (21 connections) — `server/models/lucidity.py`
- **rescue_service.py** (20 connections) — `server/services/rescue_service.py`
- **LucidityAdjustmentLog** (19 connections) — `server/models/lucidity.py`
- **asyncio** (17 connections)
- **_MockAsyncSession** (16 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **lucidity_repository.py** (13 connections) — `server/services/lucidity_repository.py`
- **RescueService** (12 connections) — `server/services/rescue_service.py`
- **_scalar_result()** (11 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **asyncio** (11 connections)
- **fixture** (10 connections)
- **UUID** (9 connections)
- **.rescue()** (8 connections) — `server/services/rescue_service.py`
- **_utc_now()** (7 connections) — `server/services/lucidity_repository.py`
- **test_get_cooldown()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_get_exposure_state()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_get_or_create_player_lucidity_existing()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_get_player_lucidity_returns_record()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_increment_exposure_state_existing()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- *... and 180 more nodes in this community*

## Relationships

- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (33 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (23 shared connections)
- [Test Rescue Commands](Test_Rescue_Commands.md) (13 shared connections)
- [Test Player Respawn Service](Test_Player_Respawn_Service.md) (12 shared connections)
- [Service](Service.md) (5 shared connections)
- [Catatonia Check](Catatonia_Check.md) (5 shared connections)
- [Database](Database.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Lucidity](Lucidity.md) (3 shared connections)
- [Test Lucidity Utils](Test_Lucidity_Utils.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Test Debrief Command](Test_Debrief_Command.md) (2 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_repository.py`
- `server/services/rescue_service.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_lucidity_repository.py`
- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 431 (89%)
- INFERRED: 53 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*