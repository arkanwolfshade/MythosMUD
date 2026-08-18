# server tests unit services test

> 21 nodes

## Key Concepts

- **test_hallucination_services.py** (24 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **asyncio** (9 connections)
- **test_check_room_entry_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_check_time_based_delegates_to_should_trigger()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_handles_lucidity_errors()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_room_entry_roll()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_cooldown_active()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_requires_session()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_time_based_triggers_and_sets_cooldown()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_unknown_tier()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **test_hallucination_frequency_wrong_trigger_type()** (4 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Unit tests for hallucination-related services (fake tells, frequency, phantoms).** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Lucidity service errors are swallowed and return False.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Room entry helper resolves tier and delegates.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Time-based helper resolves tier and delegates.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Unknown tier never triggers.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Tier with mismatched trigger type never triggers.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Room entry uses probability roll without session.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Time-based checks return False when session is missing.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Active cooldown blocks time-based trigger.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **Expired cooldown allows roll; trigger sets new cooldown.** (1 connections) — `server/tests/unit/services/test_hallucination_services.py`

## Relationships

- [server models lucidity lucidityactioncode](server_models_lucidity_lucidityactioncode.md) (11 shared connections)
- [server services phantom hostile service](server_services_phantom_hostile_service.md) (5 shared connections)
- [server services fake hallucination service](server_services_fake_hallucination_service.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_hallucination_services.py`

## Audit Trail

- EXTRACTED: 42 (82%)
- INFERRED: 9 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*