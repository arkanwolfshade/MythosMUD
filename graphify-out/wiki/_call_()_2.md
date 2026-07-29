# . call ()

> 16 nodes

## Key Concepts

- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **DecodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **EncodeLiabilitiesFn** (7 connections) — `server/utils/liability_types.py`
- **_RandomChoiceSource** (6 connections) — `server/services/player_respawn_service.py`
- **.choice()** (3 connections) — `server/services/player_respawn_service.py`
- **.__call__()** (3 connections) — `server/utils/liability_types.py`
- **LiabilityStackEntry** (3 connections)
- **.__call__()** (3 connections) — `server/utils/liability_types.py`
- **Protocol** (2 connections)
- **Subset of random.Random / random module API used for liability picks.** (1 connections) — `server/services/player_respawn_service.py`
- **Return one element from a non-empty sequence of liability codes.** (1 connections) — `server/services/player_respawn_service.py`
- **Increase existing liability stacks or add one liability if none exist.** (1 connections) — `server/services/player_respawn_service.py`
- **Callable that parses liability JSON into normalized stack entries.** (1 connections) — `server/utils/liability_types.py`
- **Decode stored liability text (or empty state) into stack rows.** (1 connections) — `server/utils/liability_types.py`
- **Callable that serializes liability stack rows for persistence.** (1 connections) — `server/utils/liability_types.py`
- **Encode stack rows into JSON suitable for PlayerLucidity.liabilities.** (1 connections) — `server/utils/liability_types.py`

## Relationships

- [. init ()](_init_%28%29.md) (10 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (5 shared connections)
- [datetime](datetime.md) (2 shared connections)

## Source Files

- `server/services/player_respawn_service.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 47 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*