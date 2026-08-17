# server services fake hallucination service

> 60 nodes

## Key Concepts

- **test_hallucination_services.py** (24 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **HallucinationFrequencyService** (20 connections) — `server/services/hallucination_frequency_service.py`
- **FakeHallucinationService** (12 connections) — `server/services/fake_hallucination_service.py`
- **hallucination_frequency_service.py** (10 connections) — `server/services/hallucination_frequency_service.py`
- **asyncio** (9 connections)
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (7 connections) — `server/services/lucidity_helpers.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **fake_hallucination_service.py** (6 connections) — `server/services/fake_hallucination_service.py`
- **UUID** (5 connections)
- **.generate_fake_npc_tell()** (4 connections) — `server/services/fake_hallucination_service.py`
- **.generate_room_text_overlay()** (4 connections) — `server/services/fake_hallucination_service.py`
- **test_check_room_entry_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_time_based_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_handles_lucidity_errors()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_room_entry_roll()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_cooldown_active()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_requires_session()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_triggers_and_sets_cooldown()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_unknown_tier()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_wrong_trigger_type()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **AsyncSession** (4 connections)
- **test_fake_hallucination_generate_npc_tell()** (3 connections) — `server/tests/unit/services/test_hallucination_services.py`
- *... and 35 more nodes in this community*

## Relationships

- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (10 shared connections)
- [server services passive lucidity flux](server_services_passive_lucidity_flux.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/services/fake_hallucination_service.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 105 (88%)
- INFERRED: 15 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*