# Community 862

> 18 nodes

## Key Concepts

- **CoreStatValues** (7 connections) — `server/models/stats_random.py`
- **roll_random_core_stat_values()** (7 connections) — `server/models/stats_random.py`
- **._ensure_core_stats()** (6 connections) — `server/models/game.py`
- **stats_random.py** (5 connections) — `server/models/stats_random.py`
- **_merge_random_core_stats()** (4 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (4 connections) — `server/models/game.py`
- **_coerce_stat_int()** (3 connections) — `server/models/game.py`
- **_needs_random_core_stats()** (3 connections) — `server/models/game.py`
- **model_validator** (3 connections)
- **TypedDict** (1 connections)
- **Generate random core stats when missing or None. Callers may pass…** (1 connections) — `server/models/game.py`
- **Convert persisted stat values to int with a safe fallback.** (1 connections) — `server/models/game.py`
- **Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes…** (1 connections) — `server/models/game.py`
- **True when any core stat key is missing or explicitly None.** (1 connections) — `server/models/game.py`
- **Fill missing or None core stat keys from rolled values.** (1 connections) — `server/models/game.py`
- **Random core stat rolls for character creation (no Stats import — breaks…** (1 connections) — `server/models/stats_random.py`
- **Core attribute ints rolled for a new character (keys match Stats core fields…** (1 connections) — `server/models/stats_random.py`
- **Roll core attribute values for a new character. Returns a plain dict so…** (1 connections) — `server/models/stats_random.py`

## Relationships

- [Community 61](Community_61.md) (6 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (3 shared connections)
- [Community 236](Community_236.md) (2 shared connections)
- [Community 391](Community_391.md) (1 shared connections)
- [Community 1063](Community_1063.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/stats_random.py`

## Audit Trail

- EXTRACTED: 31 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*