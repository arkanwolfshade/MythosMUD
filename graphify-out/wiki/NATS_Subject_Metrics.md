# NATS Subject Metrics

> 18 nodes

## Key Concepts

- **._check_dict_condition()** (6 connections) — `server/models/npc.py`
- **._spawn_value_allows_spawn()** (6 connections) — `server/models/npc.py`
- **._single_spawn_condition_ok()** (5 connections) — `server/models/npc.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **._check_missing_key_condition()** (3 connections) — `server/models/npc.py`
- **._check_list_condition()** (3 connections) — `server/models/npc.py`
- **._game_value_below_bound()** (3 connections) — `server/models/npc.py`
- **._game_value_above_bound()** (3 connections) — `server/models/npc.py`
- **._check_simple_condition()** (3 connections) — `server/models/npc.py`
- **Check if missing key condition is acceptable.          Returns:             True** (1 connections) — `server/models/npc.py`
- **Check list condition.          Returns:             True if condition passes, Fa** (1 connections) — `server/models/npc.py`
- **True if numeric game_value is strictly below bound.** (1 connections) — `server/models/npc.py`
- **True if numeric game_value is strictly above bound.** (1 connections) — `server/models/npc.py`
- **Check dict (range) condition.** (1 connections) — `server/models/npc.py`
- **Check simple value condition.          Returns:             True if condition pa** (1 connections) — `server/models/npc.py`
- **Return False if this condition value blocks spawning; True otherwise.** (1 connections) — `server/models/npc.py`
- **Evaluate one key from spawn_conditions; False means spawn blocked.** (1 connections) — `server/models/npc.py`
- **Check if current game state meets spawn conditions.** (1 connections) — `server/models/npc.py`

## Relationships

- [Command Parser Tests](Command_Parser_Tests.md) (9 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (2 shared connections)

## Source Files

- `server/models/npc.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*