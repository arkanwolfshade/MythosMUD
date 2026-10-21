# .create_instance

> 5 nodes · cohesion 0.40

## Key Concepts

- **.validate_target_player()** (4 connections) — `server/models/command_player_state.py`
- **.validate_modifier()** (4 connections) — `server/models/command_player_state.py`
- **field_validator** (2 connections)
- **Validate optional modifier for the lie command.** (1 connections) — `server/models/command_player_state.py`
- **Validate the target player name using shared validation rules.** (1 connections) — `server/models/command_player_state.py`

## Relationships

- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [test_look_item_helpers.py](test_look_item_helpers.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/models/command_player_state.py`

## Audit Trail

- EXTRACTED: 7 (88%)
- INFERRED: 1 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*