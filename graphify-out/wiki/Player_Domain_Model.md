# Player Domain Model

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

- [Player Death Service Tests](Player_Death_Service_Tests.md) (10 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (6 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (6 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (4 shared connections)
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (4 shared connections)
- [Metadata Npc](Metadata_Npc.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (2 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (1 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (1 shared connections)

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