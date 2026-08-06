# lucidity services helpers

> 56 nodes

## Key Concepts

- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **UUID** (6 connections)
- **_format_liabilities()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_max_lcd()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_liabilities()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_reason_and_source()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_metadata()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_string_player_id()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_dispatch_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_current_lcd()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_message()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_with_rescuer_and_target()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_catatonia_event_dispatch_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_basic()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_with_all_fields()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_with_progress_only()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_rescue_update_event_dispatch_error()** (3 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- *... and 31 more nodes in this community*

## Relationships

- [room conftest toolkit](room_conftest_toolkit.md) (9 shared connections)
- [player room realtime](player_room_realtime.md) (8 shared connections)
- [command factories create](command_factories_create.md) (7 shared connections)
- [Spell Validation](Spell_Validation.md) (7 shared connections)
- [npc population stats](npc_population_stats.md) (3 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 219 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*