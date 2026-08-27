# logging_file_setup.py

> 24 nodes

## Key Concepts

- **hallucination_frequency_service.py** (10 connections) — `server/services/hallucination_frequency_service.py`
- **HallucinationFrequencyService** (8 connections) — `server/services/hallucination_frequency_service.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **LucidityActionCode** (6 connections) — `server/models/lucidity.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **._time_based_hallucination_due()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **resolve_tier()** (6 connections) — `server/services/lucidity_helpers.py`
- **UUID** (5 connections)
- **AsyncSession** (4 connections)
- **worsened_tier()** (3 connections) — `server/services/lucidity_helpers.py`
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
- **Return True when the new tier is worse than the previous tier.** (1 connections) — `server/services/lucidity_helpers.py`

## Relationships

- [look_command.py](look_command.py.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (1 shared connections)
- [test_party_service.py](test_party_service.py.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`

## Audit Trail

- EXTRACTED: 44 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*