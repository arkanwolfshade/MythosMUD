# Command Player State

> 5 nodes

## Key Concepts

- **.validate_target_player()** (4 connections) — `server/models/command_player_state.py`
- **.validate_modifier()** (3 connections) — `server/models/command_player_state.py`
- **field_validator** (2 connections)
- **Validate optional modifier for the lie command.** (1 connections) — `server/models/command_player_state.py`
- **Validate the target player name using shared validation rules.** (1 connections) — `server/models/command_player_state.py`

## Relationships

- [Command Aliases](Command_Aliases.md) (2 shared connections)
- [Security Validators](Security_Validators.md) (1 shared connections)

## Source Files

- `server/models/command_player_state.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*