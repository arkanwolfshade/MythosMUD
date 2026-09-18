# Community 464

> 38 nodes

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
- **test_handle_fake_hallucination_npc_tell()** (5 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_fake_hallucination_room_overlay()** (5 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_phantom_hostile_hallucination()** (5 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_uneasy_room_entry_hallucination_delivers_overlay_only()** (5 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_phantom_path()** (4 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_no_record()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_wrong_tier()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **AsyncSession** (1 connections)
- **Deliver the requested hallucination type via the real handler functions.** (1 connections) — `server/commands/admin_hallucinate_command.py`
- **Select which type of fake hallucination to trigger (50/50 chance). Returns:…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Service for generating fake NPC tells and room text overlays. These…** (1 connections) — `server/services/fake_hallucination_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [Community 345](Community_345.md) (6 shared connections)
- [Community 544](Community_544.md) (6 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (6 shared connections)
- [Community 160](Community_160.md) (6 shared connections)
- [Community 38](Community_38.md) (5 shared connections)
- [Community 693](Community_693.md) (4 shared connections)
- [Community 1194](Community_1194.md) (2 shared connections)
- [Community 217](Community_217.md) (2 shared connections)
- [Community 289](Community_289.md) (1 shared connections)
- [Community 260](Community_260.md) (1 shared connections)

## Source Files

- `server/commands/admin_hallucinate_command.py`
- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 101 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*