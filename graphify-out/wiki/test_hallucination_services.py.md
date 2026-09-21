# test_hallucination_services.py

> 89 nodes

## Key Concepts

- **test_hallucination_services.py** (27 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **HallucinationFrequencyService** (22 connections) — `server/services/hallucination_frequency_service.py`
- **PhantomHostileService** (18 connections) — `server/services/phantom_hostile_service.py`
- **hallucination_frequency_service.py** (11 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (9 connections) — `server/services/lucidity_helpers.py`
- **asyncio** (9 connections)
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **_mock_rng()** (7 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **LucidityActionCode** (6 connections) — `server/models/lucidity.py`
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
- *... and 64 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [LucidityService](LucidityService.md) (8 shared connections)
- [admin_hallucinate_command.py](admin_hallucinate_command.py.md) (7 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (2 shared connections)
- [debrief_command.py](debrief_command.py.md) (1 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 152 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*