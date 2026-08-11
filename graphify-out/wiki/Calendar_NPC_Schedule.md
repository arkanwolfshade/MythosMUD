# Calendar NPC Schedule

> 36 nodes

## Key Concepts

- **lucidity.py** (33 connections) — `server/models/lucidity.py`
- **HallucinationFrequencyService** (10 connections) — `server/services/hallucination_frequency_service.py`
- **hallucination_frequency_service.py** (9 connections) — `server/services/hallucination_frequency_service.py`
- **_utc_now()** (8 connections) — `server/models/lucidity.py`
- **LucidityActionCode** (8 connections) — `server/models/lucidity.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **test_lucidity_utils.py** (7 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (5 connections)
- **AsyncSession** (4 connections)
- **test_utc_now_returns_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_naive_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_utc_time()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_different_times()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **datetime** (2 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **StrEnum** (1 connections)
- **Lucidity tracking models drawn from the Pnakotic Manuscripts.** (1 connections) — `server/models/lucidity.py`
- **Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibi** (1 connections) — `server/models/lucidity.py`
- **Action codes used for lucidity cooldowns (debrief, hallucination timer, etc.).** (1 connections) — `server/models/lucidity.py`
- **Any** (1 connections)
- **Hallucination frequency service for MythosMUD.  Implements tier-based hallucinat** (1 connections) — `server/services/hallucination_frequency_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (14 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (3 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (3 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (2 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (2 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (1 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (1 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (1 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/tests/unit/models/test_lucidity_utils.py`

## Audit Trail

- EXTRACTED: 142 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*