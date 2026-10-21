# PopulationStats

> 172 nodes · cohesion 0.02

## Key Concepts

- **LucidityService** (86 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (76 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (56 connections) — `server/services/lucidity_service.py`
- **lucidity_helpers.py** (28 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_service.py** (27 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **CatatoniaObserverProtocol** (24 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_trigger_handlers.py** (18 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **LucidityUpdateResult** (17 connections) — `server/services/lucidity_helpers.py`
- **asyncio** (16 connections)
- **handle_catatonia_transitions()** (14 connections) — `server/services/lucidity_trigger_handlers.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **test_lucidity_round_trip.py** (12 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **test_lucidity_adjustment_round_trip()** (12 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **UUID** (11 connections)
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **asyncio** (9 connections)
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- *... and 147 more nodes in this community*

## Relationships

- [test_command_registry_consistency.py](test_command_registry_consistency.py.md) (30 shared connections)
- [FollowService](FollowService.md) (20 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (17 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (15 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (11 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (9 shared connections)
- [test_security_headers.py](test_security_headers.py.md) (8 shared connections)
- [ui-v2/types.ts](ui-v2-types.ts.md) (8 shared connections)
- [Room](Room.md) (7 shared connections)
- [test_command_communication.py](test_command_communication.py.md) (6 shared connections)
- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (6 shared connections)
- [Hardening Dimensions](Hardening_Dimensions.md) (5 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 481 (87%)
- INFERRED: 69 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*