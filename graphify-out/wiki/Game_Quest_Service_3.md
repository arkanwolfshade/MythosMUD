# Game Quest Service

> 10 nodes · cohesion 0.20

## Key Concepts

- **_make_turn_in_definition_row()** (6 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_inventory_full_blocks_item_reward()** (4 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_no_active_instance_returns_error()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_success()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_wrong_entity_returns_error()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **Definition with auto_complete false and turn_in_entities.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **turn_in applies rewards and sets instance completed when goals met and at valid** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **turn_in returns error when at_entity_id not in turn_in_entities.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **turn_in returns error when player has no active instance.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **When reward is item and inventory full, turn_in returns error (block turn-in).** (1 connections) — `server/tests/unit/game/test_quest_service.py`

## Relationships

- [[Game Quest Service]] (5 shared connections)
- [[Quest Service Core]] (1 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
