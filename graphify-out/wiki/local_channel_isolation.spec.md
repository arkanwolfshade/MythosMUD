# local channel isolation.spec

> 15 nodes

## Key Concepts

- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **UUID** (6 connections)
- **test_send_catatonia_event_dispatch_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_with_all_fields()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Helpers for broadcasting lucidity-related SSE events.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Send an event to a specific player, swallowing transport errors in headless test** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Emit a catatonia state event to the affected player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Send rescue progress/status updates to either participant.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Send a hallucination event to a player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Test send_catatonia_event handles dispatch errors gracefully.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_rescue_update_event with all optional fields.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Relationships

- [main()](main%28%29.md) (16 shared connections)
- [25 30% Critical Regression Tests](25_30%25_Critical_Regression_Tests.md) (12 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (4 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [Personal system chat maps target](Personal_system_chat_maps_target.md) (1 shared connections)
- [test_dispatch_player_event_uuid_conversion](test_dispatch_player_event_uuid_conversion.md) (1 shared connections)
- [test_send_catatonia_event_basic](test_send_catatonia_event_basic.md) (1 shared connections)
- [test_send_rescue_update_event_dispatch_error](test_send_rescue_update_event_dispatch_error.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 85 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*