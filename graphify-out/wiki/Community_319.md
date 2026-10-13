# Community 319

> 52 nodes

## Key Concepts

- **hallucinations.py** (16 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **FakeHallucinationService** (15 connections) — `server/services/fake_hallucination_service.py`
- **deliver_personal_system()** (10 connections) — `server/game/chat_npc_system.py`
- **handle_fake_hallucination()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_hallucination_triggers()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_room_text_overlay_hallucination()** (10 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **send_hallucination_event()** (9 connections) — `server/services/lucidity_event_dispatcher.py`
- **handle_phantom_hostile_hallucination()** (9 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (9 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **asyncio** (7 connections)
- **UUID** (6 connections)
- **handle_uneasy_room_entry_hallucination()** (5 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
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

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (11 shared connections)
- [Community 177](Community_177.md) (6 shared connections)
- [Community 301](Community_301.md) (5 shared connections)
- [Community 438](Community_438.md) (4 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (2 shared connections)
- [Community 206](Community_206.md) (2 shared connections)
- [Community 568](Community_568.md) (1 shared connections)

## Source Files

- `server/game/chat_npc_system.py`
- `server/services/fake_hallucination_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 113 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*