# LucidityService

> 82 nodes · cohesion 0.04

## Key Concepts

- **LucidityService** (78 connections) — `server/services/lucidity_service.py`
- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **LucidityAdjustmentLog** (23 connections) — `server/models/lucidity.py`
- **active_lucidity_service.py** (22 connections) — `server/services/active_lucidity_service.py`
- **handle_debrief_command()** (16 connections) — `server/commands/debrief_command.py`
- **UUID** (14 connections)
- **test_lucidity_service.py** (11 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **UnknownEncounterCategoryError** (10 connections) — `server/services/active_lucidity_service.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **Any** (8 connections)
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **LucidityActionError** (7 connections) — `server/services/active_lucidity_service.py`
- **test_lucidity_adjustment_round_trip()** (7 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **_generate_narrative_recap()** (6 connections) — `server/commands/debrief_command.py`
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- **.add_liability()** (6 connections) — `server/services/lucidity_service.py`
- **test_lucidity_service_smoke.py** (6 connections) — `server/tests/unit/test_lucidity_service_smoke.py`
- **_check_debrief_availability()** (5 connections) — `server/commands/debrief_command.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (5 connections) — `server/commands/debrief_command.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **._default_liability_picker()** (5 connections) — `server/services/lucidity_service.py`
- **_get_catatonia_registry_from_app()** (4 connections) — `server/commands/debrief_command.py`
- **_get_persistence_from_app()** (4 connections) — `server/commands/debrief_command.py`
- **_validate_debrief_context()** (4 connections) — `server/commands/debrief_command.py`
- *... and 57 more nodes in this community*

## Relationships

- [lucidity_service.py](lucidity_service.py.md) (28 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (18 shared connections)
- [test_lucidity_models.py](test_lucidity_models.py.md) (18 shared connections)
- [PlayerLucidity](PlayerLucidity.md) (15 shared connections)
- [Player](Player.md) (11 shared connections)
- [AliasStorage](AliasStorage.md) (10 shared connections)
- [lucidity.py](lucidity.py.md) (10 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [__init__.py](__init__.py.md) (5 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_service.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_active_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 355 (90%)
- INFERRED: 41 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*