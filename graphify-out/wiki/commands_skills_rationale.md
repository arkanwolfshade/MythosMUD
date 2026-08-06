# commands skills rationale

> 6 nodes

## Key Concepts

- **add_default_combat_data_to_stats()** (9 connections) — `server/schemas/combat/combat_schema.py`
- **test_add_default_combat_data_to_stats()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **test_add_default_combat_data_to_stats_preserves_existing()** (3 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **Add default combat data to base_stats if not present.      Args:         stats:** (1 connections) — `server/schemas/combat/combat_schema.py`
- **Test add_default_combat_data_to_stats() adds defaults.** (1 connections) — `server/tests/unit/schemas/test_combat_schema.py`
- **Test add_default_combat_data_to_stats() preserves existing values.** (1 connections) — `server/tests/unit/schemas/test_combat_schema.py`

## Relationships

- [admin auth service](admin_auth_service.md) (5 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [skill game service](skill_game_service.md) (1 shared connections)

## Source Files

- `server/schemas/combat/combat_schema.py`
- `server/tests/unit/schemas/test_combat_schema.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*