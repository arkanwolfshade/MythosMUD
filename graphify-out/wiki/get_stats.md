# .get_stats

> 22 nodes

## Key Concepts

- **.get_stats()** (13 connections) — `server/models/player.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- **.get_combat_stats()** (4 connections) — `server/models/player.py`
- **.get_health_percentage()** (4 connections) — `server/models/player.py`
- **.get_health_state()** (4 connections) — `server/models/player.py`
- **.is_alive()** (4 connections) — `server/models/player.py`
- **.is_dead()** (4 connections) — `server/models/player.py`
- **.is_mortally_wounded()** (4 connections) — `server/models/player.py`
- **Get player stats as dictionary. Returns a MutableDict instance that…** (1 connections) — `server/models/player.py`
- **Set player stats from dictionary. Accepts both plain dict and MutableDict…** (1 connections) — `server/models/player.py`
- **Check if player is alive (DP > 0).** (1 connections) — `server/models/player.py`
- **Check if player is mortally wounded (0 >= DP > -10). Returns: True if player…** (1 connections) — `server/models/player.py`
- **Check if player is dead (DP <= -10). Returns: True if player has -10 DP or below** (1 connections) — `server/models/player.py`
- **Get player's current health state. Returns: "alive" if DP > 0…** (1 connections) — `server/models/player.py`
- **Get stats used for combat participant creation. Returns current_dp, max_dp, and…** (1 connections) — `server/models/player.py`
- **Get player determination points (DP) as percentage.** (1 connections) — `server/models/player.py`
- **Apply DP decay (e.g. mortally wounded bleeding) with posture updates. Decreases…** (1 connections) — `server/models/player.py`
- **Restore player to full health (max DP, standing posture). Used on respawn. Sets…** (1 connections) — `server/models/player.py`
- **Apply a DP change (e.g. from combat sync) with posture updates. Updates…** (1 connections) — `server/models/player.py`

## Relationships

- [Player](Player.md) (11 shared connections)
- [coerce_int](coerce_int.md) (9 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/models/player.py`

## Audit Trail

- EXTRACTED: 44 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*