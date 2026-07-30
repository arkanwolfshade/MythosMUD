# UUID

> 19 nodes

## Key Concepts

- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **handle_debrief_command()** (16 connections) — `server/commands/debrief_command.py`
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

- [main()](main%28%29.md) (11 shared connections)
- [Player Position Service](Player_Position_Service.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)
- [CommandHandler](CommandHandler.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)

## Source Files

- `server/commands/debrief_command.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*