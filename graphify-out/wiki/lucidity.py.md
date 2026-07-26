# lucidity.py

> 32 nodes · cohesion 0.09

## Key Concepts

- **lucidity.py** (33 connections) — `server/models/lucidity.py`
- **hallucination_frequency_service.py** (9 connections) — `server/services/hallucination_frequency_service.py`
- **HallucinationFrequencyService** (9 connections) — `server/services/hallucination_frequency_service.py`
- **LucidityActionCode** (8 connections) — `server/models/lucidity.py`
- **_utc_now()** (8 connections) — `server/models/lucidity.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **test_lucidity_utils.py** (7 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (4 connections)
- **AsyncSession** (3 connections)
- **test_utc_now_returns_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_different_times()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_naive_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_utc_time()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **datetime** (2 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **StrEnum** (1 connections)
- **Lucidity tracking models drawn from the Pnakotic Manuscripts.** (1 connections) — `server/models/lucidity.py`
- **Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibi** (1 connections) — `server/models/lucidity.py`
- **Action codes used for lucidity cooldowns (debrief, hallucination timer, etc.).** (1 connections) — `server/models/lucidity.py`
- **Hallucination frequency service for MythosMUD.  Implements tier-based hallucinat** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger on room entry (Uneasy tier).          Args** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (10 shared connections)
- [Player](Player.md) (6 shared connections)
- [lucidity_service.py](lucidity_service.py.md) (6 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (4 shared connections)
- [test_lucidity_models.py](test_lucidity_models.py.md) (4 shared connections)
- [Base](Base.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [hallucinations.py](hallucinations.py.md) (2 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (1 shared connections)
- [__init__.py](__init__.py.md) (1 shared connections)
- [PassiveLucidityFluxService](PassiveLucidityFluxService.md) (1 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/tests/unit/models/test_lucidity_utils.py`

## Audit Trail

- EXTRACTED: 126 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*