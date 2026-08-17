# server commands admin setlucidity command

> 295 nodes

## Key Concepts

- **LucidityService** (75 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (66 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **lucidity.py** (35 connections) — `server/models/lucidity.py`
- **admin_setlucidity_command.py** (31 connections) — `server/commands/admin_setlucidity_command.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_lucidity_repository.py** (25 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_lucidity_service.py** (25 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **LucidityExposureState** (24 connections) — `server/models/lucidity.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **active_lucidity_service.py** (23 connections) — `server/services/active_lucidity_service.py`
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **LucidityAdjustmentLog** (20 connections) — `server/models/lucidity.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_trigger_handlers.py** (18 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **LucidityActionOnCooldownError** (17 connections) — `server/services/active_lucidity_service.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **_MockAsyncSession** (16 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **lucidity_repository.py** (13 connections) — `server/services/lucidity_repository.py`
- **asyncio** (13 connections)
- **LucidityUpdateResult** (12 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- *... and 270 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (43 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (26 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (20 shared connections)
- [server commands debrief command check](server_commands_debrief_command_check.md) (16 shared connections)
- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (13 shared connections)
- [server game skill service](server_game_skill_service.md) (11 shared connections)
- [server commands lucidity recovery commands](server_commands_lucidity_recovery_commands.md) (11 shared connections)
- [server services fake hallucination service](server_services_fake_hallucination_service.md) (10 shared connections)
- [baseevent](baseevent.md) (9 shared connections)
- [server services passive lucidity flux](server_services_passive_lucidity_flux.md) (8 shared connections)
- [asyncsessionfactory](asyncsessionfactory.md) (8 shared connections)
- [server commands inventory command coercion](server_commands_inventory_command_coercion.md) (6 shared connections)

## Source Files

- `server/commands/admin_setlucidity_command.py`
- `server/commands/debrief_command.py`
- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_lucidity_repository.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 721 (87%)
- INFERRED: 110 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*