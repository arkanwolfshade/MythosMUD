# npc idle movement

> 4 nodes

## Key Concepts

- **test_create_player_with_stats_name_exists()** (4 connections) — `server/tests/unit/game/test_player_service.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **Get the modifier for a given attribute (standard D&D-style calculation).** (1 connections) — `server/models/game.py`
- **Test create_player_with_stats() when name already exists.** (1 connections) — `server/tests/unit/game/test_player_service.py`

## Relationships

- [player service game](player_service_game.md) (2 shared connections)
- [command factories communication](command_factories_communication.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [player event state](player_event_state.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/game/test_player_service.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*