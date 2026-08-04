# services service phantom

> 101 nodes

## Key Concepts

- **test_hallucination_services.py** (23 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **HallucinationFrequencyService** (19 connections) — `server/services/hallucination_frequency_service.py`
- **PhantomHostileService** (17 connections) — `server/services/phantom_hostile_service.py`
- **hallucinations.py** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (12 connections) — `server/services/fake_hallucination_service.py`
- **hallucination_frequency_service.py** (10 connections) — `server/services/hallucination_frequency_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **LucidityActionCode** (8 connections) — `server/models/lucidity.py`
- **test_passive_lucidity_hallucinations.py** (8 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **handle_phantom_hostile_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_fake_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (5 connections)
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **UUID** (4 connections)
- **UUID** (4 connections)
- **UUID** (3 connections)
- **AsyncSession** (3 connections)
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- *... and 76 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (9 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (3 shared connections)
- [player room realtime](player_room_realtime.md) (2 shared connections)
- [combat services persistence](combat_services_persistence.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/fake_hallucination_service.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 309 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*