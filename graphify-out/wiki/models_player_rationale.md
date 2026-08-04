# models player rationale

> 26 nodes

## Key Concepts

- **_stats_int()** (16 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **test_stats_int_delegates_to_coerce_int()** (3 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **Coerce a JSONB stat value to int for DP and combat helpers.** (1 connections) — `server/models/player.py`
- **Get player stats as dictionary.          Returns a MutableDict instance that aut** (1 connections) — `server/models/player.py`
- **Set player stats from dictionary.          Accepts both plain dict and MutableDi** (1 connections) — `server/models/player.py`
- **Check if player is alive (DP > 0).** (1 connections) — `server/models/player.py`
- **Check if player is mortally wounded (0 >= DP > -10).          Returns:** (1 connections) — `server/models/player.py`
- **Check if player is dead (DP <= -10).          Returns:             True if playe** (1 connections) — `server/models/player.py`
- **Get player's current health state.          Returns:             "alive" if DP >** (1 connections) — `server/models/player.py`
- **Get stats used for combat participant creation.          Returns current_dp, max** (1 connections) — `server/models/player.py`
- **Get player determination points (DP) as percentage.** (1 connections) — `server/models/player.py`
- **Apply DP decay (e.g. mortally wounded bleeding) with posture updates.          D** (1 connections) — `server/models/player.py`
- **Restore player to full health (max DP, standing posture).          Used on respa** (1 connections) — `server/models/player.py`
- **Apply a DP change (e.g. from combat sync) with posture updates.          Updates** (1 connections) — `server/models/player.py`
- *... and 1 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (12 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (3 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (1 shared connections)
- [player persistence repository](player_persistence_repository.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`

## Audit Trail

- EXTRACTED: 89 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*