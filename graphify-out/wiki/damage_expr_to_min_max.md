# damage_expr_to_min_max

> 31 nodes

## Key Concepts

- **damage_expr_to_min_max()** (14 connections) — `server/game/dice_expr.py`
- **dice_expr.py** (13 connections) — `server/game/dice_expr.py`
- **roll_damage_expr()** (11 connections) — `server/game/dice_expr.py`
- **test_dice_expr.py** (10 connections) — `server/tests/unit/game/test_dice_expr.py`
- **damage_expr.py** (5 connections) — `server/game/items/damage_expr.py`
- **_parse_terms()** (4 connections) — `server/game/dice_expr.py`
- **_term_roll()** (4 connections) — `server/game/dice_expr.py`
- **_strip_trailing_alpha()** (3 connections) — `server/game/dice_expr.py`
- **_term_minmax()** (3 connections) — `server/game/dice_expr.py`
- **test_damage_expr_to_min_max()** (3 connections) — `server/tests/unit/game/test_dice_expr.py`
- **test_roll_damage_expr_within_bounds()** (3 connections) — `server/tests/unit/game/test_dice_expr.py`
- **test_damage_expr.py** (3 connections) — `server/tests/unit/game/items/test_damage_expr.py`
- **_secrets_roll()** (2 connections) — `server/game/dice_expr.py`
- **test_items_damage_expr_reexports_shared_helper()** (2 connections) — `server/tests/unit/game/items/test_damage_expr.py`
- **test_damage_expr_rejects_empty()** (2 connections) — `server/tests/unit/game/test_dice_expr.py`
- **test_damage_expr_rejects_unparseable()** (2 connections) — `server/tests/unit/game/test_dice_expr.py`
- **test_roll_damage_expr_deterministic()** (2 connections) — `server/tests/unit/game/test_dice_expr.py`
- **test_roll_damage_expr_rejects_empty()** (2 connections) — `server/tests/unit/game/test_dice_expr.py`
- **Random** (2 connections)
- **_RollInt** (1 connections)
- **parametrize** (1 connections)
- **Shared damage_expr helpers for catalog dual-write and combat rolls. Used by…** (1 connections) — `server/game/dice_expr.py`
- **Inclusive lo..hi using secrets (avoids Bandit/Codacy B311 on random).** (1 connections) — `server/game/dice_expr.py`
- **Roll a dice expression once and return a non-negative integer. Args: expr: Dice…** (1 connections) — `server/game/dice_expr.py`
- **Drop trailing +DB / -flavor suffixes until none remain.** (1 connections) — `server/game/dice_expr.py`
- *... and 6 more nodes in this community*

## Relationships

- [npcs/catalog_dml.py](npcs-catalog_dml.py.md) (3 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (3 shared connections)
- [catalog_dml.py](catalog_dml.py.md) (2 shared connections)

## Source Files

- `server/game/dice_expr.py`
- `server/game/items/damage_expr.py`
- `server/tests/unit/game/items/test_damage_expr.py`
- `server/tests/unit/game/test_dice_expr.py`

## Audit Trail

- EXTRACTED: 53 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*