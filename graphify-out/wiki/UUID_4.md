# UUID

> 42 nodes

## Key Concepts

- **hallucinations.py** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **PhantomHostileService** (12 connections) — `server/services/phantom_hostile_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (8 connections) — `server/services/fake_hallucination_service.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
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
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **Any** (2 connections)
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.__init__()** (2 connections) — `server/services/phantom_hostile_service.py`
- **.should_spawn_phantom_hostile()** (2 connections) — `server/services/phantom_hostile_service.py`
- **Service for generating fake NPC tells and room text overlays.      These halluci** (1 connections) — `server/services/fake_hallucination_service.py`
- **Initialize the fake hallucination service.** (1 connections) — `server/services/fake_hallucination_service.py`
- **Generate a fake NPC tell hallucination.          Args:             player_id: Pl** (1 connections) — `server/services/fake_hallucination_service.py`
- *... and 17 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (6 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (3 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [config](config.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`

## Audit Trail

- EXTRACTED: 128 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*