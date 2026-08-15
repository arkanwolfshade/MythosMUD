# PhantomHostileService

> 65 nodes

## Key Concepts

- **PhantomHostileService** (17 connections) — `server/services/phantom_hostile_service.py`
- **handle_hallucination_triggers()** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **hallucinations.py** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (12 connections) — `server/services/fake_hallucination_service.py`
- **handle_fake_hallucination()** (8 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (8 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **handle_phantom_hostile_hallucination()** (7 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **asyncio** (6 connections)
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (5 connections)
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **UUID** (4 connections)
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **test_fake_hallucination_generate_npc_tell()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_generate_room_overlay()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_select_type()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_create_track_remove_clear()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_generate_name()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_deranged()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_fractured()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- *... and 40 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (3 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 107 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*