# test_metrics_endpoints.py

> 84 nodes · cohesion 0.04

## Key Concepts

- **test_hallucination_services.py** (27 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **HallucinationFrequencyService** (22 connections) — `server/services/hallucination_frequency_service.py`
- **PhantomHostileService** (18 connections) — `server/services/phantom_hostile_service.py`
- **hallucination_frequency_service.py** (11 connections) — `server/services/hallucination_frequency_service.py`
- **HallucinationRng** (9 connections) — `server/services/hallucination_rng.py`
- **asyncio** (9 connections)
- **hallucination_rng.py** (8 connections) — `server/services/hallucination_rng.py`
- **_mock_rng()** (7 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **PhantomData** (6 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (6 connections)
- **test_hallucination_rng.py** (6 connections) — `server/tests/unit/services/test_hallucination_rng.py`
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **.find_phantom_by_name_in_room()** (5 connections) — `server/services/phantom_hostile_service.py`
- **test_hallucination_frequency_room_entry_roll()** (5 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_triggers_and_sets_cooldown()** (5 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **.get()** (4 connections) — `server/services/hallucination_rng.py`
- **.get_active_phantoms()** (4 connections) — `server/services/phantom_hostile_service.py`
- **test_check_room_entry_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_time_based_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_select_type()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_handles_lucidity_errors()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_cooldown_active()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_requires_session()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_unknown_tier()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_wrong_trigger_type()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- *... and 59 more nodes in this community*

## Relationships

- [Room](Room.md) (9 shared connections)
- [Hardening Dimensions](Hardening_Dimensions.md) (5 shared connections)
- [test_config_models.py](test_config_models.py.md) (5 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)
- [test_command_registry_consistency.py](test_command_registry_consistency.py.md) (2 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (2 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (1 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (1 shared connections)
- [look_container.py](look_container.py.md) (1 shared connections)

## Source Files

- `server/services/hallucination_frequency_service.py`
- `server/services/hallucination_rng.py`
- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_rng.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 144 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*