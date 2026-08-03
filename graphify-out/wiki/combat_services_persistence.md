# combat services persistence

> 19 nodes

## Key Concepts

- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **handle_debrief_command()** (15 connections) — `server/commands/debrief_command.py`
- **Any** (8 connections)
- **_generate_narrative_recap()** (6 connections) — `server/commands/debrief_command.py`
- **_check_debrief_availability()** (5 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (5 connections) — `server/commands/debrief_command.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **_get_persistence_from_app()** (4 connections) — `server/commands/debrief_command.py`
- **_get_catatonia_registry_from_app()** (4 connections) — `server/commands/debrief_command.py`
- **_validate_debrief_context()** (4 connections) — `server/commands/debrief_command.py`
- **Debrief command for MythosMUD.  After sanitarium failover (LCD -100), players mu** (1 connections) — `server/commands/debrief_command.py`
- **Retrieve persistence service from app container or state.** (1 connections) — `server/commands/debrief_command.py`
- **Retrieve catatonia registry from app container or state.** (1 connections) — `server/commands/debrief_command.py`
- **Validate persistence and player existence for debrief command.** (1 connections) — `server/commands/debrief_command.py`
- **Check if debrief cooldown exists and return error if not available.** (1 connections) — `server/commands/debrief_command.py`
- **Perform therapy session if requested and append result to message.** (1 connections) — `server/commands/debrief_command.py`
- **Complete debrief by clearing cooldown and finalizing message.** (1 connections) — `server/commands/debrief_command.py`
- **Handle the debrief command after sanitarium failover.      Provides narrative re** (1 connections) — `server/commands/debrief_command.py`
- **Generate narrative recap of recent events leading to sanitarium intervention.** (1 connections) — `server/commands/debrief_command.py`

## Relationships

- [commands admin mute](commands_admin_mute.md) (9 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)

## Source Files

- `server/commands/debrief_command.py`

## Audit Trail

- EXTRACTED: 88 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*