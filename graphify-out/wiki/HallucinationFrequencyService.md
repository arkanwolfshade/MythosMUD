# HallucinationFrequencyService

> 17 nodes

## Key Concepts

- **HallucinationFrequencyService** (10 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (5 connections)
- **AsyncSession** (4 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Tier** (2 connections)
- **Any** (1 connections)
- **Check if hallucination should trigger on room entry (Uneasy tier). Args:…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Initialize the hallucination frequency service.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if a hallucination should trigger based on tier and frequency rules.…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Derive tier label based on LCD thresholds.** (1 connections) — `server/services/lucidity_helpers.py`

## Relationships

- [LucidityService](LucidityService.md) (6 shared connections)
- [hallucinations.py](hallucinations.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`

## Audit Trail

- EXTRACTED: 33 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*