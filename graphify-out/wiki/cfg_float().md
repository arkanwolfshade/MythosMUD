# cfg float()

> 87 nodes

## Key Concepts

- **IdleMovementHandler** (60 connections) — `server/npc/idle_movement.py`
- **test_idle_movement.py** (35 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **.should_idle_move()** (5 connections) — `server/npc/idle_movement.py`
- **_passes_movement_probability()** (4 connections) — `server/npc/idle_movement.py`
- **._npc_registered_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/idle_movement.py`
- **._try_idle_room_change()** (4 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_uuid()** (3 connections) — `server/npc/idle_movement.py`
- **._check_npc_combat_via_string_mapping()** (3 connections) — `server/npc/idle_movement.py`
- **.get_valid_exits()** (3 connections) — `server/npc/idle_movement.py`
- **._log_idle_move_outcome()** (3 connections) — `server/npc/idle_movement.py`
- **idle_movement_handler()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_idle_movement_handler_init_no_persistence()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_disabled()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_alive()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_not_active()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_check()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_passes_when_random_below_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_probability_fails_when_random_above_threshold()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_false_when_registered_in_combat()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **test_should_idle_move_true_when_not_in_combat_and_probability_succeeds()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- *... and 62 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (7 shared connections)
- [cfg bool()](cfg_bool%28%29.md) (7 shared connections)
- [.initialize()](initialize%28%29.md) (5 shared connections)
- [. is npc in combat()](_is_npc_in_combat%28%29.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [. repr ()](_repr_%28%29.md) (2 shared connections)
- [.get active status effects()](get_active_status_effects%28%29.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 283 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*