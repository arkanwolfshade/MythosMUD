# auth endpoints rationale

> 177 nodes

## Key Concepts

- **LucidityService** (88 connections) — `server/services/lucidity_service.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **debrief_command.py** (26 connections) — `server/commands/debrief_command.py`
- **test_debrief_command.py** (25 connections) — `server/tests/unit/commands/test_debrief_command.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_service.py** (24 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **active_lucidity_service.py** (23 connections) — `server/services/active_lucidity_service.py`
- **ActiveLucidityService** (20 connections) — `server/services/active_lucidity_service.py`
- **handle_debrief_command()** (19 connections) — `server/commands/debrief_command.py`
- **UUID** (14 connections)
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **_generate_narrative_recap()** (10 connections) — `server/commands/debrief_command.py`
- **UnknownEncounterCategoryError** (10 connections) — `server/services/active_lucidity_service.py`
- **LucidityUpdateResult** (10 connections) — `server/services/lucidity_helpers.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **_perform_therapy_if_requested()** (9 connections) — `server/commands/debrief_command.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **Any** (8 connections)
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **_validate_debrief_context()** (7 connections) — `server/commands/debrief_command.py`
- **_check_debrief_availability()** (7 connections) — `server/commands/debrief_command.py`
- *... and 152 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (45 shared connections)
- [zone configuration npc](zone_configuration_npc.md) (16 shared connections)
- [Spell Validation](Spell_Validation.md) (16 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (10 shared connections)
- [room renderer functions](room_renderer_functions.md) (10 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [npc population control](npc_population_control.md) (8 shared connections)
- [npc population stats](npc_population_stats.md) (8 shared connections)
- [command factories create](command_factories_create.md) (7 shared connections)
- [models player rationale](models_player_rationale.md) (6 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (4 shared connections)
- [container schemas containers](container_schemas_containers.md) (4 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/commands/test_debrief_command.py`
- `server/tests/unit/services/test_lucidity_service.py`

## Audit Trail

- EXTRACTED: 747 (93%)
- INFERRED: 52 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*