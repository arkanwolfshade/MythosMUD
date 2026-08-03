# lucidity models rationale

> 37 nodes

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
- **Tier** (6 connections)
- **UUID** (4 connections)
- **AsyncSession** (3 connections)
- **test_utc_now_returns_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_naive_datetime()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_utc_time()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_utc_now_returns_different_times()** (3 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **datetime** (2 connections)
- **.__init__()** (2 connections) — `server/services/hallucination_frequency_service.py`
- **AsyncSession** (2 connections)
- **Tier** (2 connections)
- **StrEnum** (1 connections)
- **Lucidity tracking models drawn from the Pnakotic Manuscripts.** (1 connections) — `server/models/lucidity.py`
- **Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibi** (1 connections) — `server/models/lucidity.py`
- **Action codes used for lucidity cooldowns (debrief, hallucination timer, etc.).** (1 connections) — `server/models/lucidity.py`
- *... and 12 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (19 shared connections)
- [world models rationale](world_models_rationale.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [combat services persistence](combat_services_persistence.md) (2 shared connections)
- [command helpers functions](command_helpers_functions.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [rescue service services](rescue_service_services.md) (2 shared connections)
- [services service phantom](services_service_phantom.md) (2 shared connections)
- [command validation commands](command_validation_commands.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (1 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (1 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/tests/unit/models/test_lucidity_utils.py`

## Audit Trail

- EXTRACTED: 136 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*