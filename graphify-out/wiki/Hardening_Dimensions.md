# Hardening Dimensions

> 13 nodes · cohesion 0.24

## Key Concepts

- **resolve_tier()** (9 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (5 connections)
- **AsyncSession** (4 connections)
- **Tier** (2 connections)
- **Any** (1 connections)
- **Check if hallucination should trigger on room entry (Uneasy tier). Args:…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if a hallucination should trigger based on tier and frequency rules.…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Derive tier label based on LCD thresholds.** (1 connections) — `server/services/lucidity_helpers.py`

## Relationships

- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (5 shared connections)
- [PopulationStats](PopulationStats.md) (5 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [FollowService](FollowService.md) (1 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`

## Audit Trail

- EXTRACTED: 27 (87%)
- INFERRED: 4 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*