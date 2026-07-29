# HallucinationFrequencyService

> 17 nodes

## Key Concepts

- **HallucinationFrequencyService** (9 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (4 connections)
- **AsyncSession** (3 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Tier** (2 connections)
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Initialize the hallucination frequency service.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if a hallucination should trigger based on tier and frequency rules.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger on room entry (Uneasy tier).          Args** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Derive tier label based on LCD thresholds.** (1 connections) — `server/services/lucidity_helpers.py`
- **Update record LCD/tier from delta; return previous and new LCD/tier values.** (1 connections) — `server/services/lucidity_service.py`

## Relationships

- [datetime](datetime.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (4 shared connections)
- [UUID](UUID.md) (3 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`

## Audit Trail

- EXTRACTED: 55 (89%)
- INFERRED: 7 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*