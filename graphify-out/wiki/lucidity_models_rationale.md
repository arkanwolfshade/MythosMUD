# lucidity models rationale

> 32 nodes

## Key Concepts

- **HallucinationFrequencyService** (19 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (4 connections)
- **AsyncSession** (3 connections)
- **test_hallucination_frequency_unknown_tier()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_wrong_trigger_type()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_room_entry_roll()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_requires_session()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_cooldown_active()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_triggers_and_sets_cooldown()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_handles_lucidity_errors()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_room_entry_delegates_to_should_trigger()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_time_based_delegates_to_should_trigger()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Initialize the hallucination frequency service.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if a hallucination should trigger based on tier and frequency rules.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger on room entry (Uneasy tier).          Args** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Derive tier label based on LCD thresholds.** (1 connections) — `server/services/lucidity_helpers.py`
- **Unknown tier never triggers.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Tier with mismatched trigger type never triggers.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- *... and 7 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (12 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (4 shared connections)
- [combat services persistence](combat_services_persistence.md) (2 shared connections)
- [services service phantom](services_service_phantom.md) (2 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 91 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*