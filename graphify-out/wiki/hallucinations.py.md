# hallucinations.py

> 52 nodes

## Key Concepts

- **hallucinations.py** (16 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (15 connections) — `server/services/fake_hallucination_service.py`
- **deliver_forced_hallucination()** (12 connections) — `server/commands/admin_hallucinate_command.py`
- **handle_hallucination_triggers()** (12 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_fake_hallucination()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_room_text_overlay_hallucination()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **send_hallucination_event()** (9 connections) — `server/services/lucidity_event_dispatcher.py`
- **handle_phantom_hostile_hallucination()** (9 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (9 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **handle_uneasy_room_entry_hallucination()** (7 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **asyncio** (7 connections)
- **UUID** (6 connections)
- **FakeNpcTellData** (4 connections) — `server/services/fake_hallucination_service.py`
- **RoomTextOverlayData** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **test_handle_fake_hallucination_npc_tell()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_fake_hallucination_room_overlay()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_phantom_hostile_hallucination()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_uneasy_room_entry_hallucination_delivers_overlay_only()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_fake_hallucination_generate_npc_tell()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_generate_room_overlay()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_handle_hallucination_triggers_no_record()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_phantom_path()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_wrong_tier()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- *... and 27 more nodes in this community*

## Relationships

- [admin_hallucinate_command.py](admin_hallucinate_command.py.md) (10 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (6 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (2 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)
- [MovementService](MovementService.md) (1 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_hallucinate_command.py`
- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 118 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*