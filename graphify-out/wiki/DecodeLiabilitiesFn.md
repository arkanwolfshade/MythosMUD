# DecodeLiabilitiesFn

> 10 nodes

## Key Concepts

- **DecodeLiabilitiesFn** (6 connections) — `server/utils/liability_types.py`
- **EncodeLiabilitiesFn** (6 connections) — `server/utils/liability_types.py`
- **.__call__()** (3 connections) — `server/utils/liability_types.py`
- **.__call__()** (3 connections) — `server/utils/liability_types.py`
- **LiabilityStackEntry** (2 connections)
- **Protocol** (2 connections)
- **Callable that parses liability JSON into normalized stack entries.** (1 connections) — `server/utils/liability_types.py`
- **Decode stored liability text (or empty state) into stack rows.** (1 connections) — `server/utils/liability_types.py`
- **Callable that serializes liability stack rows for persistence.** (1 connections) — `server/utils/liability_types.py`
- **Encode stack rows into JSON suitable for PlayerLucidity.liabilities.** (1 connections) — `server/utils/liability_types.py`

## Relationships

- [Player](Player.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (2 shared connections)
- [LucidityService](LucidityService.md) (2 shared connections)

## Source Files

- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*