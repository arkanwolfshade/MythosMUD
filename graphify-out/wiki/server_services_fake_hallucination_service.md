# server services fake hallucination service

> 18 nodes

## Key Concepts

- **FakeHallucinationService** (12 connections) — `server/services/fake_hallucination_service.py`
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **test_fake_hallucination_generate_npc_tell()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_generate_room_overlay()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_fake_hallucination_select_type()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **UUID** (3 connections)
- **.__init__()** (2 connections) — `server/services/fake_hallucination_service.py`
- **.select_hallucination_type()** (2 connections) — `server/services/fake_hallucination_service.py`
- **Any** (2 connections)
- **Generate a room text overlay hallucination. Args: player_id: Player UUID who…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Select which type of fake hallucination to trigger (50/50 chance). Returns:…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Service for generating fake NPC tells and room text overlays. These…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Initialize the fake hallucination service.** (1 connections) — `server/services/fake_hallucination_service.py`
- **Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will…** (1 connections) — `server/services/fake_hallucination_service.py`
- **Fake tell includes npc name, message, room, and hallucination id.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Room overlay includes text, room, and hallucination id.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Selection returns one of the two hallucination types.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (4 shared connections)
- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*