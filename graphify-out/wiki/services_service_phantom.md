# services service phantom

> 56 nodes

## Key Concepts

- **hallucinations.py** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **PhantomHostileService** (12 connections) — `server/services/phantom_hostile_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **hallucination_frequency_service.py** (9 connections) — `server/services/hallucination_frequency_service.py`
- **HallucinationFrequencyService** (9 connections) — `server/services/hallucination_frequency_service.py`
- **FakeHallucinationService** (8 connections) — `server/services/fake_hallucination_service.py`
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
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- *... and 31 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (7 shared connections)
- [lucidity event services](lucidity_event_services.md) (3 shared connections)
- [services passive lucidity](services_passive_lucidity.md) (2 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`

## Audit Trail

- EXTRACTED: 177 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*