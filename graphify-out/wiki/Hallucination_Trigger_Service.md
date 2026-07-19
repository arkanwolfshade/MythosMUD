# Hallucination Trigger Service

> 40 nodes · cohesion 0.07

## Key Concepts

- **hallucinations.py** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **PhantomHostileService** (12 connections) — `server/services/phantom_hostile_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (8 connections) — `server/services/fake_hallucination_service.py`
- **handle_fake_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_phantom_hostile_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **UUID** (5 connections) — `server/services/phantom_hostile_service.py`
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (4 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **UUID** (3 connections) — `server/services/fake_hallucination_service.py`
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **Any** (2 connections) — `server/services/fake_hallucination_service.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.__init__()** (2 connections) — `server/services/phantom_hostile_service.py`
- **.should_spawn_phantom_hostile()** (2 connections) — `server/services/phantom_hostile_service.py`
- **Hallucination trigger handling for passive lucidity flux.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Check and handle time-based hallucination triggers.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Handle phantom hostile spawn hallucination.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Handle fake hallucination (NPC tells or room text overlays).** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- *... and 15 more nodes in this community*

## Relationships

- [[NPC Admin API]] (6 shared connections)
- [[Lucidity Event Dispatcher]] (3 shared connections)
- [[Performance Monitor Metrics]] (3 shared connections)
- [[Services Hallucination Frequency]] (2 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`

## Audit Trail

- EXTRACTED: 119 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
