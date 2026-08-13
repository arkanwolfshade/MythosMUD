# patch

> 17 nodes

## Key Concepts

- **patch** (8 connections)
- **test_is_npc_in_combat_true()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_active()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_check()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_true_when_not_in_combat_and_probability_succeeds()** (4 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Movement runs when random.random() <= idle_movement_probability (exclusive…** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Movement is skipped when random.random() > idle_movement_probability.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Gating skips idle movement when combat service lists this NPC.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **When combat service is empty and probability passes, idle move is allowed.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test _is_npc_in_combat() when NPC is in combat.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() returns False when NPC is not alive.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() returns False when NPC is not active.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test should_idle_move() respects movement probability (random > threshold…** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`

## Relationships

- [IdleMovementHandler](IdleMovementHandler.md) (8 shared connections)
- [test_idle_movement.py](test_idle_movement.py.md) (8 shared connections)

## Source Files

- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*