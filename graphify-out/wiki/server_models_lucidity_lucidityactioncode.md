# server models lucidity lucidityactioncode

> 22 nodes

## Key Concepts

- **HallucinationFrequencyService** (20 connections) — `server/services/hallucination_frequency_service.py`
- **hallucination_frequency_service.py** (10 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **LucidityActionCode** (6 connections) — `server/models/lucidity.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (5 connections)
- **AsyncSession** (4 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **Tier** (2 connections)
- **StrEnum** (1 connections)
- **Any** (1 connections)
- **Action codes used for lucidity cooldowns (debrief, hallucination timer, etc.).** (1 connections) — `server/models/lucidity.py`
- **Hallucination frequency service for MythosMUD. Implements tier-based…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger on room entry (Uneasy tier). Args:…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if hallucination should trigger based on time (Fractured/Deranged tiers).…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Initialize the hallucination frequency service.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Check if a hallucination should trigger based on tier and frequency rules.…** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Derive tier label based on LCD thresholds.** (1 connections) — `server/services/lucidity_helpers.py`

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (11 shared connections)
- [server models lucidity](server_models_lucidity.md) (10 shared connections)
- [server constants spawn defaults](server_constants_spawn_defaults.md) (2 shared connections)
- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands debrief command](server_commands_debrief_command.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`

## Audit Trail

- EXTRACTED: 47 (78%)
- INFERRED: 13 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*