# server services lucidity event dispatcher

> 21 nodes

## Key Concepts

- **handle_hallucination_triggers()** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **hallucinations.py** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (9 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **handle_fake_hallucination()** (8 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **handle_phantom_hostile_hallucination()** (7 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **asyncio** (6 connections)
- **UUID** (4 connections)
- **test_handle_fake_hallucination_npc_tell()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_fake_hallucination_room_overlay()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_no_record()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_phantom_path()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_wrong_tier()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_phantom_hostile_hallucination()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **AsyncSession** (1 connections)
- **Send a hallucination event to a player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Hallucination trigger handling for passive lucidity flux.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Check and handle time-based hallucination triggers.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Handle phantom hostile spawn hallucination.** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Handle fake hallucination (NPC tells or room text overlays).** (1 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **Unit tests for passive lucidity flux hallucination triggers.** (1 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Relationships

- [server models lucidity](server_models_lucidity.md) (3 shared connections)
- [server services phantom hostile service](server_services_phantom_hostile_service.md) (3 shared connections)
- [passivelucidityfluxservice](passivelucidityfluxservice.md) (3 shared connections)
- [server services fake hallucination service](server_services_fake_hallucination_service.md) (2 shared connections)
- [server models lucidity lucidityactioncode](server_models_lucidity_lucidityactioncode.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*