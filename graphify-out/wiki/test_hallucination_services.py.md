# test_hallucination_services.py

> 43 nodes

## Key Concepts

- **test_hallucination_services.py** (24 connections) — `server/tests/unit/services/test_hallucination_services.py`
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
- **test_phantom_create_track_remove_clear()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_generate_name()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_deranged()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_fractured()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Any** (1 connections)
- **Check if hallucination should trigger on room entry (Uneasy tier). Args:…** (1 connections) — `server/services/hallucination_frequency_service.py`
- *... and 18 more nodes in this community*

## Relationships

- [PhantomHostileService](PhantomHostileService.md) (7 shared connections)
- [LucidityService](LucidityService.md) (7 shared connections)
- [FakeHallucinationService](FakeHallucinationService.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 73 (82%)
- INFERRED: 16 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*