# conftest BoundLogger rationale

> 2 nodes

## Key Concepts

- **test_select_exit_single_exit()** (3 connections) — `server/tests/unit/npc/test_idle_movement.py`
- **Test select_exit() with single exit.** (1 connections) — `server/tests/unit/npc/test_idle_movement.py`

## Relationships

- [config models player](config_models_player.md) (1 shared connections)
- [idle movement npc](idle_movement_npc.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_idle_movement.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*