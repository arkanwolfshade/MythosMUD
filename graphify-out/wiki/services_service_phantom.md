# services service phantom

> 62 nodes

## Key Concepts

- **PhantomHostileService** (17 connections) — `server/services/phantom_hostile_service.py`
- **hallucinations.py** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (12 connections) — `server/services/fake_hallucination_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (8 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **handle_phantom_hostile_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_fake_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (5 connections)
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **UUID** (4 connections)
- **UUID** (3 connections)
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **test_fake_hallucination_generate_npc_tell()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_generate_room_overlay()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_select_type()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_fractured()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_deranged()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_generate_name()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_create_track_remove_clear()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (15 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (3 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (2 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 173 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*