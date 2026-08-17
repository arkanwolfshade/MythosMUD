# player_combat_service

> 9 nodes

## Key Concepts

- **player_combat_service()** (7 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **fixture** (4 connections)
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **mock_npc_service()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock persistence layer.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock event bus.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create mock NPC combat integration service (no _rewards so XP uses fallback…** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **Create PlayerCombatService instance.** (1 connections) — `server/tests/unit/services/test_player_combat_service.py`

## Relationships

- [test_player_combat_service.py](test_player_combat_service.py.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [SpellRegistry](SpellRegistry.md) (1 shared connections)
- [combat_loader.py](combat_loader.py.md) (1 shared connections)
- [test_go_command.py](test_go_command.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 12 (75%)
- INFERRED: 4 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*