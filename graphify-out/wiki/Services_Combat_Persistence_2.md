# Services Combat Persistence

> 14 nodes

## Key Concepts

- **HallucinationFrequencyService** (10 connections) — `server/services/hallucination_frequency_service.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (5 connections)
- **AsyncSession** (4 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Any** (1 connections)
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Initialize the hallucination frequency service.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if a hallucination should trigger based on tier and frequency rules.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger on room entry (Uneasy tier).          Args** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).** (1 connections) — `server/services/hallucination_frequency_service.py`

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (6 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (2 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`

## Audit Trail

- EXTRACTED: 49 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*