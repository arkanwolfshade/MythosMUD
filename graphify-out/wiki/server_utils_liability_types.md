# server utils liability types

> 12 nodes

## Key Concepts

- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **DecodeLiabilitiesFn** (4 connections) — `server/utils/liability_types.py`
- **EncodeLiabilitiesFn** (4 connections) — `server/utils/liability_types.py`
- **.__call__()** (3 connections) — `server/utils/liability_types.py`
- **.__call__()** (3 connections) — `server/utils/liability_types.py`
- **LiabilityStackEntry** (2 connections)
- **Protocol** (2 connections)
- **Shared TypedDicts for liability JSON stored on PlayerLucidity.liabilities.** (1 connections) — `server/utils/liability_types.py`
- **Callable that parses liability JSON into normalized stack entries.** (1 connections) — `server/utils/liability_types.py`
- **Decode stored liability text (or empty state) into stack rows.** (1 connections) — `server/utils/liability_types.py`
- **Callable that serializes liability stack rows for persistence.** (1 connections) — `server/utils/liability_types.py`
- **Encode stack rows into JSON suitable for PlayerLucidity.liabilities.** (1 connections) — `server/utils/liability_types.py`

## Relationships

- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (2 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*