# LucidityService

> 84 nodes

## Key Concepts

- **LucidityService** (82 connections) — `server/services/lucidity_service.py`
- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_debrief_command.py** (25 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **handle_debrief_command()** (19 connections) — `server/commands/debrief_command.py`
- **UUID** (12 connections)
- **_generate_narrative_recap()** (9 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (9 connections) — `server/commands/debrief_command.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **asyncio** (9 connections)
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **Any** (8 connections)
- **_check_debrief_availability()** (7 connections) — `server/commands/debrief_command.py`
- **_validate_debrief_context()** (7 connections) — `server/commands/debrief_command.py`
- **._calculate_max_lcd()** (7 connections) — `server/services/lucidity_service.py`
- **_get_catatonia_registry_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **_get_persistence_from_app()** (6 connections) — `server/commands/debrief_command.py`
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- **.add_liability()** (6 connections) — `server/services/lucidity_service.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **._max_lcd_from_stats()** (5 connections) — `server/services/lucidity_service.py`
- **.set_cooldown()** (5 connections) — `server/services/lucidity_service.py`
- **test_handle_debrief_command_success()** (5 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_perform_therapy_on_cooldown()** (5 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **test_lucidity_service_apply_adjustment()** (5 connections) — `server/tests/unit/test_lucidity_service_smoke.py`
- **.get_cooldown()** (4 connections) — `server/services/lucidity_service.py`
- *... and 59 more nodes in this community*

## Relationships

- [Player](Player.md) (30 shared connections)
- [test_lucidity_service.py](test_lucidity_service.py.md) (19 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (10 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (8 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (6 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/lucidity_service.py`
- `server/tests/unit/commands/test_debrief_command.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 221 (86%)
- INFERRED: 36 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*