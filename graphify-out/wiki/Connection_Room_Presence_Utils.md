# Connection Room Presence Utils

> 33 nodes

## Key Concepts

- **_stats_int()** (17 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **UUID** (9 connections)
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (8 connections) — `server/app/game_tick_processing.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **_player_in_active_combat()** (4 connections) — `server/app/game_tick_processing.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **test_stats_int_delegates_to_coerce_int()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **Return True when the player is in an active combat (skip passive DP decay).** (1 connections) — `server/app/game_tick_processing.py`
- **Move player to limbo and publish authoritative DP when death threshold is reache** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single mortally wounded player's DP decay and death check.      CRITIC** (1 connections) — `server/app/game_tick_processing.py`
- **Coerce a JSONB stat value to int for DP and combat helpers.** (1 connections) — `server/models/player.py`
- **Get player stats as dictionary.          Returns a MutableDict instance that aut** (1 connections) — `server/models/player.py`
- **Set player stats from dictionary.          Accepts both plain dict and MutableDi** (1 connections) — `server/models/player.py`
- **Check if player is alive (DP > 0).** (1 connections) — `server/models/player.py`
- **Check if player is mortally wounded (0 >= DP > -10).          Returns:** (1 connections) — `server/models/player.py`
- *... and 8 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (12 shared connections)
- [Command Alias Handling](Command_Alias_Handling.md) (7 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (5 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (3 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`

## Audit Trail

- EXTRACTED: 122 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*