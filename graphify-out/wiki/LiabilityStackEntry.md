# LiabilityStackEntry

> 137 nodes

## Key Concepts

- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **rescue_commands.py** (31 connections) — `server/commands/rescue_commands.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **rescue_service.py** (16 connections) — `server/services/rescue_service.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **LucidityUpdateResult** (7 connections) — `server/services/lucidity_helpers.py`
- **UUID** (6 connections)
- **LucidityChangeEventContext** (6 connections) — `server/services/lucidity_helpers.py`
- *... and 112 more nodes in this community*

## Relationships

- [UUID](UUID.md) (29 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (13 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (13 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (13 shared connections)
- [map helpers](map_helpers.md) (9 shared connections)
- [emote](emote.md) (8 shared connections)
- [test command factories communication](test_command_factories_communication.md) (6 shared connections)
- [clean command input()](clean_command_input%28%29.md) (4 shared connections)
- [config](config.md) (3 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/services/rescue_service.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 602 (99%)
- INFERRED: 7 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*