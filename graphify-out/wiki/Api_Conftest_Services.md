# Api Conftest Services

> 5 nodes · cohesion 0.40

## Key Concepts

- **Create a mock persistence layer.** (4 connections) — `server/tests/unit/api/conftest.py`
- **mock_async_persistence()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/api/conftest.py`
- **mock_async_persistence()** (2 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`

## Relationships

- [[API Test Fixtures]] (1 shared connections)
- [[Look Command Helpers]] (1 shared connections)
- [[NPC Combat Lifecycle]] (1 shared connections)
- [[NPC Combat Integration]] (1 shared connections)
- [[Npc Services Combat]] (1 shared connections)
- [[NPC Combat Player Attack]] (1 shared connections)

## Source Files

- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
