# Hallucination Trigger Service

> 44 nodes · cohesion 0.06

## Key Concepts

- **hallucinations.py** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **PhantomHostileService** (12 connections) — `server/services/phantom_hostile_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (8 connections) — `server/services/fake_hallucination_service.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **handle_fake_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_phantom_hostile_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **phantom_hostile_service.py** (5 connections) — `server/services/phantom_hostile_service.py`
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (5 connections)
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **UUID** (4 connections)
- **UUID** (3 connections)
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **Any** (2 connections)
- **.__init__()** (2 connections) — `server/services/phantom_hostile_service.py`
- **.should_spawn_phantom_hostile()** (2 connections) — `server/services/phantom_hostile_service.py`
- **Generate a room text overlay hallucination.          Args:             player_id** (1 connections) — `server/services/fake_hallucination_service.py`
- **Select which type of fake hallucination to trigger (50/50 chance).          Retu** (1 connections) — `server/services/fake_hallucination_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (6 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (3 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`

## Audit Trail

- EXTRACTED: 134 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*