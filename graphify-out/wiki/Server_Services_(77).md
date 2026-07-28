# Server Services (77)

> 20 nodes

## Key Concepts

- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_hallucination_event()** (7 connections) — `server/services/lucidity_event_dispatcher.py`
- **UUID** (6 connections)
- **test_send_catatonia_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_current_lcd()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_message()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_rescuer_and_target()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_dispatch_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_import_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_uuid_conversion()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_catatonia_event with basic parameters.** (2 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Send an event to a specific player, swallowing transport errors in headless test** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Emit a catatonia state event to the affected player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Send a hallucination event to a player.** (1 connections) — `server/services/lucidity_event_dispatcher.py`
- **Test send_catatonia_event with current_lcd.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_catatonia_event with rescuer and target names.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test send_catatonia_event handles dispatch errors gracefully.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test _dispatch_player_event handles import errors gracefully.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **Test _dispatch_player_event converts UUID to string.** (1 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Relationships

- [Server Services (40)](Server_Services_%2840%29.md) (11 shared connections)
- [Server Services](Server_Services.md) (8 shared connections)
- [Server Services (53)](Server_Services_%2853%29.md) (3 shared connections)
- [Server Realtime (48)](Server_Realtime_%2848%29.md) (1 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*