# npc population stats

> 36 nodes

## Key Concepts

- **PhantomHostileService** (17 connections) — `server/services/phantom_hostile_service.py`
- **hallucinations.py** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (12 connections) — `server/services/fake_hallucination_service.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
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
- **Send a hallucination event to a player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **AsyncSession** (1 connections)
- **Hallucination trigger handling for passive lucidity flux.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Handle phantom hostile spawn hallucination.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- *... and 11 more nodes in this community*

## Relationships

- [services service phantom](services_service_phantom.md) (11 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (3 shared connections)
- [container main rationale](container_main_rationale.md) (2 shared connections)
- [command parser rationale](command_parser_rationale.md) (2 shared connections)
- [security headers middleware](security_headers_middleware.md) (1 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`

## Audit Trail

- EXTRACTED: 123 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*