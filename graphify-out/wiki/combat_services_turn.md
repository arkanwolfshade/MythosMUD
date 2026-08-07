# combat services turn

> 77 nodes

## Key Concepts

- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **.is_active()** (5 connections) — `server/models/game.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/invite.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **.is_alive()** (4 connections) — `server/npc/npc_base.py`
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
- **.add_status_effect()** (3 connections) — `server/models/game.py`
- **.remove_status_effect()** (3 connections) — `server/models/game.py`
- *... and 52 more nodes in this community*

## Relationships

- [rate limiter realtime](rate_limiter_realtime.md) (15 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (7 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [System Metrics](System_Metrics.md) (3 shared connections)
- [idle movement npc](idle_movement_npc.md) (2 shared connections)
- [player room realtime](player_room_realtime.md) (1 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/invite.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 241 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*