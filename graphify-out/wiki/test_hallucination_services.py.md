# test_hallucination_services.py

> 82 nodes

## Key Concepts

- **test_hallucination_services.py** (27 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **HallucinationFrequencyService** (22 connections) — `server/services/hallucination_frequency_service.py`
- **PhantomHostileService** (18 connections) — `server/services/phantom_hostile_service.py`
- **hallucination_frequency_service.py** (11 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (9 connections) — `server/services/lucidity_helpers.py`
- **asyncio** (9 connections)
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **_mock_rng()** (7 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **PhantomData** (6 connections) — `server/services/phantom_hostile_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (6 connections)
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **.find_phantom_by_name_in_room()** (5 connections) — `server/services/phantom_hostile_service.py`
- **test_hallucination_frequency_room_entry_roll()** (5 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_triggers_and_sets_cooldown()** (5 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **UUID** (5 connections)
- **.get_active_phantoms()** (4 connections) — `server/services/phantom_hostile_service.py`
- **test_check_room_entry_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_time_based_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_select_type()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_handles_lucidity_errors()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_cooldown_active()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_requires_session()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- *... and 57 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [hallucinations.py](hallucinations.py.md) (6 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (1 shared connections)
- [admin_hallucinate_command.py](admin_hallucinate_command.py.md) (1 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [HallucinationRng](HallucinationRng.md) (1 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 143 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*