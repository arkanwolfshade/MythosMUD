# map helpers

> 34 nodes

## Key Concepts

- **lucidity.py** (33 connections) — `server/models/lucidity.py`
- **hallucination_frequency_service.py** (9 connections) — `server/services/hallucination_frequency_service.py`
- **HallucinationFrequencyService** (9 connections) — `server/services/hallucination_frequency_service.py`
- **_utc_now()** (8 connections) — `server/models/lucidity.py`
- **LucidityActionCode** (8 connections) — `server/models/lucidity.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **.should_trigger_hallucination()** (7 connections) — `server/services/hallucination_frequency_service.py`
- **test_lucidity_utils.py** (7 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **.check_room_entry_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **.check_time_based_hallucination()** (6 connections) — `server/services/hallucination_frequency_service.py`
- **UUID** (4 connections)
- **AsyncSession** (3 connections)
- **test_utc_now_returns_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_naive_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_utc_time()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_different_times()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **datetime** (2 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **StrEnum** (1 connections)
- **Lucidity tracking models drawn from the Pnakotic Manuscripts.** (1 connections) — `server/models/lucidity.py`
- **Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibi** (1 connections) — `server/models/lucidity.py`
- **Action codes used for lucidity cooldowns (debrief, hallucination timer, etc.).** (1 connections) — `server/models/lucidity.py`
- **Hallucination frequency service for MythosMUD.  Implements tier-based hallucinat** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Service for managing hallucination frequency checks based on player tier.** (1 connections) — `server/services/hallucination_frequency_service.py`
- **Initialize the hallucination frequency service.** (1 connections) — `server/services/hallucination_frequency_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [UUID](UUID.md) (12 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (9 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (6 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [CommandExecutionRequest](CommandExecutionRequest.md) (1 shared connections)
- [config](config.md) (1 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (1 shared connections)
- [test command factories communication](test_command_factories_communication.md) (1 shared connections)
- [emote](emote.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/tests/unit/models/test_lucidity_utils.py`

## Audit Trail

- EXTRACTED: 132 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*