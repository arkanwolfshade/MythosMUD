# MessageBatcher

> 14 nodes · cohesion 0.16

## Key Concepts

- **Protocol** (6 connections)
- **_CatalogPersistence** (4 connections) — `server/commands/catalog_commands.py`
- **_CatalogPlayer** (4 connections) — `server/commands/catalog_commands.py`
- **_CatalogRequest** (4 connections) — `server/commands/catalog_commands.py`
- **.app()** (4 connections) — `server/commands/catalog_commands.py`
- **_CatalogApp** (3 connections) — `server/commands/catalog_commands.py`
- **_CatalogContainer** (3 connections) — `server/commands/catalog_commands.py`
- **.get_player_by_name()** (3 connections) — `server/commands/catalog_commands.py`
- **_CatalogAppState** (2 connections) — `server/commands/catalog_commands.py`
- **Player fields used for admin projection checks.** (1 connections) — `server/commands/catalog_commands.py`
- **Async persistence surface for admin lookup.** (1 connections) — `server/commands/catalog_commands.py`
- **Look up a player by character name.** (1 connections) — `server/commands/catalog_commands.py`
- **Container fields used by /catalog.** (1 connections) — `server/commands/catalog_commands.py`
- **FastAPI app carrying the DI container.** (1 connections) — `server/commands/catalog_commands.py`

## Relationships

- [send_system_message](send_system_message.md) (6 shared connections)
- [properties](properties.md) (1 shared connections)
- [test_room_environment_parity.py](test_room_environment_parity.py.md) (1 shared connections)

## Source Files

- `server/commands/catalog_commands.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*