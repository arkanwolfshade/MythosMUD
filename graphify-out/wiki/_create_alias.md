# _create_alias

> 4 nodes

## Key Concepts

- **_create_alias()** (5 connections) — `server/commands/alias_commands.py`
- **_validate_alias_params()** (3 connections) — `server/commands/alias_commands.py`
- **Validate alias name and command. Returns error dict if invalid, None if valid.** (1 connections) — `server/commands/alias_commands.py`
- **Create or update an alias. Returns result dict.** (1 connections) — `server/commands/alias_commands.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [handle_alias_command](handle_alias_command.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/commands/alias_commands.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*