# get user db()

> 2 nodes

## Key Concepts

- **party_service()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **PartyService with no dependencies (in-memory only).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [test command factories player state](test_command_factories_player_state.md) (1 shared connections)
- [test party service](test_party_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*