# persistence constants rationale

> 2 nodes

## Key Concepts

- **handler()** (3 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Create a MagicCommandHandler instance.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`

## Relationships

- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_magic_commands.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*