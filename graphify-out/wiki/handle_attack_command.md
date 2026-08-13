# .handle_attack_command

> 8 nodes

## Key Concepts

- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- **.handle_flee_command()** (4 connections) — `server/commands/combat_handler.py`
- **Any** (4 connections)
- **Extract command type and target name from command_data. Public API.** (1 connections) — `server/commands/combat_handler.py`
- **Extract command type and target name from command_data.** (1 connections) — `server/commands/combat_handler.py`
- **Handle attack commands (attack, punch, kick, etc.).** (1 connections) — `server/commands/combat_handler.py`
- **Handle /flee command: leave combat and move to random adjacent room.** (1 connections) — `server/commands/combat_handler.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [combat_attack.py](combat_attack.py.md) (1 shared connections)
- [TauntCommandHandler](TauntCommandHandler.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*