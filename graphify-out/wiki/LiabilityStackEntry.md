# LiabilityStackEntry

> 18 nodes

## Key Concepts

- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_max_lcd()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_liabilities()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_reason_and_source()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_metadata()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_string_player_id()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_dispatch_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Optional lucidity change event fields (reduces send_lucidity_change_event parame** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Notify a player that their LCD changed.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Test send_lucidity_change_event with basic parameters.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_lucidity_change_event with custom max_lcd.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_lucidity_change_event with liabilities.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_lucidity_change_event with reason and source.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_lucidity_change_event with metadata.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_lucidity_change_event with string player_id.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_lucidity_change_event handles dispatch errors gracefully.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Relationships

- [25 30% Critical Regression Tests](25_30%25_Critical_Regression_Tests.md) (9 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [local channel isolation.spec](local_channel_isolation.spec.md) (4 shared connections)
- [seed e2e users](seed_e2e_users.md) (2 shared connections)
- [Personal system chat maps target](Personal_system_chat_maps_target.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 62 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*