# Lucidity Rescue Helpers

> 56 nodes · cohesion 0.06

## Key Concepts

- **lucidity_service.py** (46 connections) — `server/services/lucidity_service.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_trigger_handlers.py** (17 connections) — `server/services/lucidity_trigger_handlers.py`
- **decode_liabilities()** (10 connections) — `server/services/lucidity_helpers.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **encode_liabilities()** (7 connections) — `server/services/lucidity_helpers.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **UUID** (6 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (6 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (5 connections) — `server/services/lucidity_helpers.py`
- **worsened_tier()** (5 connections) — `server/services/lucidity_helpers.py`
- **.clear_liability()** (5 connections) — `server/services/lucidity_service.py`
- **handle_delirium_trigger()** (5 connections) — `server/services/lucidity_trigger_handlers.py`
- **datetime** (4 connections) — `server/services/lucidity_helpers.py`
- **CatatoniaObserverProtocol** (4 connections) — `server/services/lucidity_trigger_handlers.py`
- **.on_catatonia_cleared()** (4 connections) — `server/services/lucidity_helpers.py`
- **.on_catatonia_entered()** (4 connections) — `server/services/lucidity_helpers.py`
- **clamp_lucidity()** (4 connections) — `server/services/lucidity_helpers.py`
- **coerce_metadata_dict()** (4 connections) — `server/services/lucidity_helpers.py`
- **lucidity_event_source()** (4 connections) — `server/services/lucidity_helpers.py`
- **normalize_metadata()** (4 connections) — `server/services/lucidity_helpers.py`
- **LiabilityStackEntry** (3 connections) — `server/services/lucidity_helpers.py`
- **.on_sanitarium_failover()** (3 connections) — `server/services/lucidity_helpers.py`
- *... and 31 more nodes in this community*

## Relationships

- [[Lucidity State Models]] (36 shared connections)
- [[Lucidity Event Dispatcher]] (14 shared connections)
- [[Lucidity Database Models]] (9 shared connections)
- [[NPC Admin API]] (7 shared connections)
- [[Integer Coercion Utils]] (5 shared connections)
- [[Alias Expansion Logic]] (3 shared connections)
- [[Ground and Rescue Commands]] (3 shared connections)
- [[Services Hallucination Frequency]] (2 shared connections)
- [[Liability . Call ()]] (2 shared connections)
- [[Services Player Respawn]] (2 shared connections)
- [[Services Rescue Service]] (1 shared connections)
- [[Lifespan Startup Hooks]] (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 254 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
