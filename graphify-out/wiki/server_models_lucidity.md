# server models lucidity

> 348 nodes

## Key Concepts

- **LucidityService** (79 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (69 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **lucidity.py** (35 connections) — `server/models/lucidity.py`
- **test_lucidity_event_dispatcher.py** (35 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **test_lucidity_repository.py** (25 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_lucidity_service.py** (25 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **LucidityExposureState** (24 connections) — `server/models/lucidity.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **asyncio** (24 connections)
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **LucidityAdjustmentLog** (20 connections) — `server/models/lucidity.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_lucidity_trigger_handlers.py** (18 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **_MockAsyncSession** (16 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **lucidity_repository.py** (13 connections) — `server/services/lucidity_repository.py`
- **asyncio** (13 connections)
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- *... and 323 more nodes in this community*

## Relationships

- [server constants spawn defaults](server_constants_spawn_defaults.md) (24 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (17 shared connections)
- [server async persistence](server_async_persistence.md) (15 shared connections)
- [passivelucidityfluxservice](passivelucidityfluxservice.md) (14 shared connections)
- [asyncsessionfactory](asyncsessionfactory.md) (13 shared connections)
- [fixturerequest](fixturerequest.md) (12 shared connections)
- [server models lucidity lucidityactioncode](server_models_lucidity_lucidityactioncode.md) (10 shared connections)
- [server commands debrief command](server_commands_debrief_command.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (7 shared connections)
- [server services active lucidity service](server_services_active_lucidity_service.md) (7 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (7 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_repository.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 820 (90%)
- INFERRED: 91 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*