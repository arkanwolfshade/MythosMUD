# Structured Error Logging

> 5 nodes · cohesion 0.40

## Key Concepts

- **test_apply_damage_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_npc_damage_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **asyncio** (4 connections)
- **Test that NPC damage is blocked when target is in login grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that damage is blocked when target is in login grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`

## Relationships

- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (2 shared connections)
- [ChatLogger](ChatLogger.md) (2 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 10 (83%)
- INFERRED: 2 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*