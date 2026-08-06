# combat services turn

> 76 nodes

## Key Concepts

- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **BaseModel** (5 connections)
- **.is_active()** (5 connections) — `server/models/game.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
- **test_player_add_item_existing()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_success()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_removes_when_zero()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_item_insufficient_quantity()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_add_status_effect()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_remove_status_effect_success()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_get_active_status_effects()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_get_active_status_effects_all_active()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_can_carry_weight_true()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_can_carry_weight_false()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_status_effect_duration_validation_min()** (4 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_min()** (4 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_max()** (4 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **.add_item()** (3 connections) — `server/models/game.py`
- **.add_status_effect()** (3 connections) — `server/models/game.py`
- **.remove_status_effect()** (3 connections) — `server/models/game.py`
- *... and 51 more nodes in this community*

## Relationships

- [player service game](player_service_game.md) (16 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (7 shared connections)
- [System Metrics](System_Metrics.md) (4 shared connections)
- [add used user](add_used_user.md) (4 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 243 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*