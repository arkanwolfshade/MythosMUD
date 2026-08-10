# Hallucination Trigger Service

> 56 nodes

## Key Concepts

- **hallucinations.py** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **PhantomHostileService** (12 connections) — `server/services/phantom_hostile_service.py`
- **HallucinationFrequencyService** (10 connections) — `server/services/hallucination_frequency_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **hallucination_frequency_service.py** (9 connections) — `server/services/hallucination_frequency_service.py`
- **FakeHallucinationService** (8 connections) — `server/services/fake_hallucination_service.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **handle_phantom_hostile_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_fake_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **UUID** (5 connections)
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (5 connections)
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **AsyncSession** (4 connections)
- **UUID** (4 connections)
- **UUID** (3 connections)
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- *... and 31 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (6 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (3 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (2 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`

## Audit Trail

- EXTRACTED: 179 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*