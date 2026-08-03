# taunt combat commands

> 20 nodes

## Key Concepts

- **.get_player_aliases()** (8 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **.remove_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias_count()** (4 connections) — `server/alias_storage.py`
- **.clear_aliases()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_name()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_command()** (3 connections) — `server/alias_storage.py`
- **Get all aliases for a player.** (1 connections) — `server/alias_storage.py`
- **Save aliases for a player.** (1 connections) — `server/alias_storage.py`
- **Add or update an alias for a player.** (1 connections) — `server/alias_storage.py`
- **Remove an alias for a player.** (1 connections) — `server/alias_storage.py`
- **Get a specific alias for a player.** (1 connections) — `server/alias_storage.py`
- **Clear all aliases for a player.** (1 connections) — `server/alias_storage.py`
- **Get the number of aliases for a player.** (1 connections) — `server/alias_storage.py`
- **Validate alias name format.** (1 connections) — `server/alias_storage.py`
- **Validate alias command.** (1 connections) — `server/alias_storage.py`
- **Create and save a new alias for a player.** (1 connections) — `server/alias_storage.py`

## Relationships

- [commands admin mute](commands_admin_mute.md) (10 shared connections)
- [alias models rationale](alias_models_rationale.md) (5 shared connections)
- [services admin auth](services_admin_auth.md) (2 shared connections)

## Source Files

- `server/alias_storage.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*