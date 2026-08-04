# error logging rationale

> 2 nodes

## Key Concepts

- **_collect_progress_sync()** (5 connections) — `server/commands/inventory_command_helpers.py`
- **Return quest_service.sync_collect_progress when it is callable.** (1 connections) — `server/commands/inventory_command_helpers.py`

## Relationships

- [inventory commands command](inventory_commands_command.md) (2 shared connections)
- [quest game service](quest_game_service.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`

## Audit Trail

- EXTRACTED: 4 (67%)
- INFERRED: 2 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*