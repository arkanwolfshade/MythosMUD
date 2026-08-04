# service combat services

> 5 nodes

## Key Concepts

- **.__init__()** (4 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (3 connections) — `server/models/game.py`
- **Any** (2 connections)
- **Initialize Stats with provided data.          For random stat generation, use ge** (1 connections) — `server/models/game.py`
- **Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes precedenc** (1 connections) — `server/models/game.py`

## Relationships

- [player service game](player_service_game.md) (2 shared connections)
- [event connection helpers](event_connection_helpers.md) (1 shared connections)

## Source Files

- `server/models/game.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*