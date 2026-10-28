# test_database_extended.py

> 76 nodes · cohesion 0.05

## Key Concepts

- **test_lucidity_event_dispatcher.py** (35 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **send_game_event()** (33 connections) — `server/realtime/connection_manager_api.py`
- **send_rescue_update_event()** (25 connections) — `server/services/lucidity_event_dispatcher.py`
- **asyncio** (25 connections)
- **lucidity_event_dispatcher.py** (22 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (19 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (14 connections) — `server/services/lucidity_event_dispatcher.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (10 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_hallucination_event()** (9 connections) — `server/services/lucidity_event_dispatcher.py`
- **UUID** (6 connections)
- **test_send_lucidity_change_event_with_liabilities()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_max_lcd()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_metadata()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_send_lucidity_change_event_with_reason_and_source()** (5 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **_format_liabilities()** (4 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_dispatch_player_event_import_error()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_dispatch_player_event_uuid_conversion()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_empty_code()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_invalid_stacks()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_entries()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_multiple_stacks()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_format_liabilities_single()** (4 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- *... and 51 more nodes in this community*

## Relationships

- [PopulationStats](PopulationStats.md) (15 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (8 shared connections)
- [look_container.py](look_container.py.md) (7 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (7 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (5 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [ManualPage.tsx](ManualPage.tsx.md) (2 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`

## Audit Trail

- EXTRACTED: 216 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*