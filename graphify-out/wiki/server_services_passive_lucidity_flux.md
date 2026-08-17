# server services passive lucidity flux

> 45 nodes

## Key Concepts

- **PhantomHostileService** (17 connections) — `server/services/phantom_hostile_service.py`
- **handle_hallucination_triggers()** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **hallucinations.py** (13 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **test_passive_lucidity_hallucinations.py** (9 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **handle_fake_hallucination()** (8 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **handle_phantom_hostile_hallucination()** (7 connections) — `server/services/passive_lucidity_flux/hallucinations.py`
- **asyncio** (6 connections)
- **.create_phantom_hostile_data()** (5 connections) — `server/services/phantom_hostile_service.py`
- **UUID** (5 connections)
- **UUID** (4 connections)
- **.clear_all_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.generate_phantom_name()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.get_active_phantoms()** (3 connections) — `server/services/phantom_hostile_service.py`
- **.remove_phantom()** (3 connections) — `server/services/phantom_hostile_service.py`
- **test_phantom_create_track_remove_clear()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_generate_name()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_deranged()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_phantom_should_spawn_fractured()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_handle_fake_hallucination_npc_tell()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_fake_hallucination_room_overlay()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_no_record()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_phantom_path()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_hallucination_triggers_wrong_tier()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **test_handle_phantom_hostile_hallucination()** (3 connections) — `server/tests/unit/services/test_passive_lucidity_hallucinations.py`
- **.__init__()** (2 connections) — `server/services/phantom_hostile_service.py`
- *... and 20 more nodes in this community*

## Relationships

- [server services fake hallucination service](server_services_fake_hallucination_service.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (3 shared connections)
- [server services passive lucidity flux](server_services_passive_lucidity_flux.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/services/passive_lucidity_flux/hallucinations.py`
- `server/services/phantom_hostile_service.py`
- `server/tests/unit/services/test_hallucination_services.py`
- `server/tests/unit/services/test_passive_lucidity_hallucinations.py`

## Audit Trail

- EXTRACTED: 82 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*