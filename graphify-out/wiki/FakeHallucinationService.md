# FakeHallucinationService

> 37 nodes

## Key Concepts

- **FakeHallucinationService** (12 connections) — `server/services/fake_hallucination_service.py`
- **handle_hallucination_triggers()** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **hallucinations.py** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (9 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **handle_fake_hallucination()** (8 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_phantom_hostile_hallucination()** (6 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **asyncio** (6 connections)
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
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
- **UUID** (3 connections)
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **Any** (2 connections)
- **AsyncSession** (1 connections)
- **Generate a room text overlay hallucination. Args: player_id: Player UUID who…** (1 connections) — `server/services/fake_hallucination_service.py`
- *... and 12 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (3 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (2 shared connections)
- [service.py](service.py.md) (2 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*