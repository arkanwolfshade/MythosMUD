# Services Hallucination Frequency

> 14 nodes · cohesion 0.22

## Key Concepts

- **HallucinationFrequencyService** (9 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (5 connections) — `server/services/hallucination_frequency_service.py`
- **AsyncSession** (4 connections) — `server/services/hallucination_frequency_service.py`
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger on room entry (Uneasy tier).          Args** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Initialize the hallucination frequency service.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if a hallucination should trigger based on tier and frequency rules.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Derive tier label based on LCD thresholds.** (1 connections) — `server/services/lucidity_helpers.py`

## Relationships

- [[Lucidity State Models]] (6 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Hallucination Trigger Service]] (2 shared connections)
- [[Lucidity Rescue Helpers]] (2 shared connections)
- [[Player Respawn Service]] (1 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`

## Audit Trail

- EXTRACTED: 45 (85%)
- INFERRED: 8 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
