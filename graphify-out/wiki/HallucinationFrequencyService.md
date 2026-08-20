# HallucinationFrequencyService

> 33 nodes

## Key Concepts

- **HallucinationFrequencyService** (20 connections) — `server/services/hallucination_frequency_service.py`
- **asyncio** (9 connections)
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (5 connections)
- **test_check_room_entry_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_time_based_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_handles_lucidity_errors()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_room_entry_roll()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_cooldown_active()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_requires_session()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_triggers_and_sets_cooldown()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_unknown_tier()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_wrong_trigger_type()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **AsyncSession** (4 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Any** (1 connections)
- **Check if hallucination should trigger on room entry (Uneasy tier). Args:…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Initialize the hallucination frequency service.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if a hallucination should trigger based on tier and frequency rules.…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Lucidity service errors are swallowed and return False.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- *... and 8 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)
- [FakeHallucinationService](FakeHallucinationService.md) (2 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 55 (82%)
- INFERRED: 12 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*