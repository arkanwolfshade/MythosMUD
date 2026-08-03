# models invite Any

> 31 nodes

## Key Concepts

- **StatusEffect** (32 connections) — `server/models/game.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **.is_active()** (5 connections) — `server/models/game.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
- **test_status_effect_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_min()** (4 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_max()** (4 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **.add_status_effect()** (3 connections) — `server/models/game.py`
- **test_status_effect_creation()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_with_source()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_permanent()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_before_duration()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_at_duration()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Represents a status effect applied to a character.** (1 connections) — `server/models/game.py`
- **Check if the status effect is still active.** (1 connections) — `server/models/game.py`
- **Add a status effect to the player.          Args:             effect: StatusEffe** (1 connections) — `server/models/game.py`
- **Get all currently active status effects.          Args:             current_tick** (1 connections) — `server/models/game.py`
- **Any** (1 connections)
- **Initialize Invite with defaults.** (1 connections) — `server/models/invite.py`
- **Unit tests for StatusEffect model.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect can be created with required fields.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect can have optional source.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns True for permanent effects (duration=0).** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- *... and 6 more nodes in this community*

## Relationships

- [command factories communication](command_factories_communication.md) (8 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [character creation service](character_creation_service.md) (3 shared connections)
- [spell game magic](spell_game_magic.md) (2 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (2 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)
- [idle npc movement](idle_npc_movement.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 100 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*