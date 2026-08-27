# Main Foyer Starting Room

> 5 nodes

## Key Concepts

- **.validate_target_player()** (4 connections) — `server/models/command_player_state.py`
- **.validate_modifier()** (3 connections) — `server/models/command_player_state.py`
- **field_validator** (2 connections)
- **Validate optional modifier for the lie command.** (1 connections) — `server/models/command_player_state.py`
- **Validate the target player name using shared validation rules.** (1 connections) — `server/models/command_player_state.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)

## Source Files

- `server/models/command_player_state.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*