# Lucidity System Expansion Scenarios

> 5 nodes

## Key Concepts

- **.get_emote_aliases()** (3 connections) — `server/persistence/repositories/emote_repository.py`
- **.get_emotes()** (3 connections) — `server/persistence/repositories/emote_repository.py`
- **Any** (2 connections)
- **Get all predefined emotes from the database. Returns: list[dict]: Rows with…** (1 connections) — `server/persistence/repositories/emote_repository.py`
- **Get all emote aliases joined to their owning emote's stable_id. Returns:…** (1 connections) — `server/persistence/repositories/emote_repository.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)

## Source Files

- `server/persistence/repositories/emote_repository.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*