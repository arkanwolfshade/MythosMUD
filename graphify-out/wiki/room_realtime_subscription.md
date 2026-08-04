# room realtime subscription

> 8 nodes

## Key Concepts

- **test_player_service_mutations.py** (34 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **test_gain_occult_knowledge_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **test_heal_player_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **test_validate_player_name_too_short_one_char()** (2 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **Unit tests for player service mutations.  Covers delete, location update, mythos** (1 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **Test gain_occult_knowledge() when player not found.** (1 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **Test heal_player() when player not found.** (1 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **Test validate_player_name() with name only 1 character.** (1 connections) — `server/tests/unit/game/test_player_service_mutations.py`

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [schemas room schema](schemas_room_schema.md) (2 shared connections)
- [schemas unified room](schemas_unified_room.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (1 shared connections)
- [MagicPointsMeter magic formatDelta()](MagicPointsMeter_magic_formatDelta%28%29.md) (1 shared connections)
- [holidays static schemas](holidays_static_schemas.md) (1 shared connections)
- [commands combat handler](commands_combat_handler.md) (1 shared connections)
- [schemas intersection schema](schemas_intersection_schema.md) (1 shared connections)
- [models invite rationale](models_invite_rationale.md) (1 shared connections)
- [archive 2025 AUDIT](archive_2025_AUDIT.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_player_service_mutations.py`

## Audit Trail

- EXTRACTED: 44 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*