# FakeHallucinationService

> 33 nodes

## Key Concepts

- **FakeHallucinationService** (12 connections) — `server/services/fake_hallucination_service.py`
- **handle_hallucination_triggers()** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **hallucinations.py** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (9 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **handle_fake_hallucination()** (8 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **handle_phantom_hostile_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **asyncio** (6 connections)
- **UUID** (4 connections)
- **test_fake_hallucination_generate_npc_tell()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_generate_room_overlay()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_select_type()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_handle_fake_hallucination_npc_tell()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_fake_hallucination_room_overlay()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_no_record()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_phantom_path()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_wrong_tier()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_phantom_hostile_hallucination()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **AsyncSession** (1 connections)
- **Select which type of fake hallucination to trigger (50/50 chance). Returns:…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Service for generating fake NPC tells and room text overlays. These…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Initialize the fake hallucination service.** (1 connections) — `server/services/fake_hallucination_service.py`
- **Send a hallucination event to a player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- *... and 8 more nodes in this community*

## Relationships

- [test_hallucination_services.py](test_hallucination_services.py.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (3 shared connections)
- [.generate_fake_npc_tell](generate_fake_npc_tell.md) (2 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*