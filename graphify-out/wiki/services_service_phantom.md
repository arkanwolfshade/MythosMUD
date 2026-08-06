# services service phantom

> 46 nodes

## Key Concepts

- **test_hallucination_services.py** (23 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **HallucinationFrequencyService** (19 connections) — `server/services/hallucination_frequency_service.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (4 connections)
- **AsyncSession** (3 connections)
- **test_fake_hallucination_generate_npc_tell()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_generate_room_overlay()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_select_type()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_unknown_tier()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_wrong_trigger_type()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_room_entry_roll()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_requires_session()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_cooldown_active()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_triggers_and_sets_cooldown()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_handles_lucidity_errors()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_room_entry_delegates_to_should_trigger()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_time_based_delegates_to_should_trigger()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_fractured()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_deranged()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_generate_name()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_create_track_remove_clear()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- *... and 21 more nodes in this community*

## Relationships

- [npc population stats](npc_population_stats.md) (11 shared connections)
- [player room realtime](player_room_realtime.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 137 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*