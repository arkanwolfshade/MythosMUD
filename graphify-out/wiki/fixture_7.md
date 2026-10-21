# fixture

> 9 nodes · cohesion 0.33

## Key Concepts

- **test_wearable_container_persistence.py** (12 connections) — `server/tests/integration/test_wearable_container_persistence.py`
- **_create_player()** (8 connections) — `server/tests/integration/test_wearable_container_persistence.py`
- **test_equip_creates_one_row_reuses_it_and_unequip_reads_it_back()** (8 connections) — `server/tests/integration/test_wearable_container_persistence.py`
- **async_sessionmaker** (2 connections)
- **AsyncSession** (2 connections)
- **UUID** (2 connections)
- **asyncio** (1 connections)
- **usefixtures** (1 connections)
- **Integration test: wearable containers against the real persistence layer…** (1 connections) — `server/tests/integration/test_wearable_container_persistence.py`

## Relationships

- [WebSocketRequestContext](WebSocketRequestContext.md) (3 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (2 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (1 shared connections)
- [CombatBroadcastMixin](CombatBroadcastMixin.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_wearable_container_persistence.py`

## Audit Trail

- EXTRACTED: 22 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*