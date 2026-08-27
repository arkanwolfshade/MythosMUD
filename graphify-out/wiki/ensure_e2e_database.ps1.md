# ensure_e2e_database.ps1

> 5 nodes

## Key Concepts

- **messaging_integration()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **fixture** (2 connections)
- **Create mock connection manager.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **Create CombatMessagingIntegration instance.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`

## Relationships

- [asyncio](asyncio.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*