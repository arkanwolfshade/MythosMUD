# Hallucination Trigger Service

> 34 nodes

## Key Concepts

- **hallucinations.py** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **PhantomHostileService** (12 connections) — `server/services/phantom_hostile_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (8 connections) — `server/services/fake_hallucination_service.py`
- **handle_phantom_hostile_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_fake_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (5 connections)
- **UUID** (4 connections)
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.__init__()** (2 connections) — `server/services/phantom_hostile_service.py`
- **.should_spawn_phantom_hostile()** (2 connections) — `server/services/phantom_hostile_service.py`
- **Service for generating fake NPC tells and room text overlays.      These halluci** (1 connections) — `server/services/fake_hallucination_service.py`
- **Initialize the fake hallucination service.** (1 connections) — `server/services/fake_hallucination_service.py`
- **Select which type of fake hallucination to trigger (50/50 chance).          Retu** (1 connections) — `server/services/fake_hallucination_service.py`
- **AsyncSession** (1 connections)
- **Hallucination trigger handling for passive lucidity flux.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Handle phantom hostile spawn hallucination.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Handle fake hallucination (NPC tells or room text overlays).** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Check and handle time-based hallucination triggers.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- *... and 9 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (5 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Services Combat Persistence](Services_Combat_Persistence.md) (2 shared connections)
- [End-to-End Validation](End-to-End_Validation.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`

## Audit Trail

- EXTRACTED: 105 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*