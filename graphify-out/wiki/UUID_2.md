# UUID

> 86 nodes

## Key Concepts

- **LucidityService** (78 connections) — `server/services/lucidity_service.py`
- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **LucidityAdjustmentLog** (23 connections) — `server/models/lucidity.py`
- **active_lucidity_service.py** (22 connections) — `server/services/active_lucidity_service.py`
- **ActiveLucidityService** (20 connections) — `server/services/active_lucidity_service.py`
- **handle_debrief_command()** (16 connections) — `server/commands/debrief_command.py`
- **UUID** (14 connections)
- **test_lucidity_service.py** (11 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **UnknownEncounterCategoryError** (10 connections) — `server/services/active_lucidity_service.py`
- **Any** (8 connections)
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **LucidityActionError** (7 connections) — `server/services/active_lucidity_service.py`
- **_generate_narrative_recap()** (6 connections) — `server/commands/debrief_command.py`
- **Tier** (6 connections)
- **._add_liabilities_for_adjustment()** (6 connections) — `server/services/lucidity_service.py`
- **.add_liability()** (6 connections) — `server/services/lucidity_service.py`
- **test_lucidity_service_smoke.py** (6 connections) — `server/tests/unit/test_lucidity_service_smoke.py`
- **_check_debrief_availability()** (5 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (5 connections) — `server/commands/debrief_command.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **worsened_tier()** (5 connections) — `server/services/lucidity_helpers.py`
- **.set_cooldown()** (5 connections) — `server/services/lucidity_service.py`
- **._default_liability_picker()** (5 connections) — `server/services/lucidity_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [test rate limiter utils](test_rate_limiter_utils.md) (30 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (26 shared connections)
- [CommandHandler](CommandHandler.md) (14 shared connections)
- [emote](emote.md) (11 shared connections)
- [map helpers](map_helpers.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (8 shared connections)
- [monitoring](monitoring.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (4 shared connections)
- [test player preferences service](test_player_preferences_service.md) (3 shared connections)
- [admin setlucidity command](admin_setlucidity_command.md) (3 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 378 (89%)
- INFERRED: 45 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*