# lucidity services helpers

> 266 nodes

## Key Concepts

- **LucidityService** (88 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (78 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **rescue_commands.py** (31 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (31 connections) — `server/commands/rescue_commands.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_service.py** (24 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_trigger_handlers.py** (17 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **rescue_service.py** (16 connections) — `server/services/rescue_service.py`
- **UUID** (14 connections)
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **RescueService** (11 connections) — `server/services/rescue_service.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **LucidityUpdateResult** (10 connections) — `server/services/lucidity_helpers.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- *... and 241 more nodes in this community*

## Relationships

- [Async Query Helpers](Async_Query_Helpers.md) (34 shared connections)
- [player room realtime](player_room_realtime.md) (31 shared connections)
- [command helpers functions](command_helpers_functions.md) (17 shared connections)
- [combat services persistence](combat_services_persistence.md) (14 shared connections)
- [NPC Combat](NPC_Combat.md) (12 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (11 shared connections)
- [combat models rationale](combat_models_rationale.md) (9 shared connections)
- [services service phantom](services_service_phantom.md) (9 shared connections)
- [commands whisper command](commands_whisper_command.md) (8 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (8 shared connections)
- [container schemas containers](container_schemas_containers.md) (6 shared connections)
- [rescue service services](rescue_service_services.md) (6 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/models/lucidity.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/services/rescue_service.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 1140 (93%)
- INFERRED: 85 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*