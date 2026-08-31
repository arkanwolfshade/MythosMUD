# .validate_current_vs_max_stats

> 19 nodes

## Key Concepts

- **.validate_current_vs_max_stats()** (6 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **.max_lucidity()** (4 connections) — `server/models/game.py`
- **.max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **computed_field** (2 connections)
- **Any** (2 connections)
- **model_validator** (2 connections)
- **Initialize Stats with provided data. For random stat generation, use…** (1 connections) — `server/models/game.py`
- **Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes…** (1 connections) — `server/models/game.py`
- **Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).…** (1 connections) — `server/models/game.py`
- **Calculate max lucidity based on education. AI: This computed field uses the…** (1 connections) — `server/models/game.py`
- **Calculate max determination points (DP) using formula: (CON + SIZ) / 5. AI:…** (1 connections) — `server/models/game.py`
- **Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).…** (1 connections) — `server/models/game.py`
- **Calculate max lucidity based on education. AI: Helper method to calculate…** (1 connections) — `server/models/game.py`
- **Ensure current_dp (DP), magic_points (MP), and lucidity don't exceed their max…** (1 connections) — `server/models/game.py`

## Relationships

- [Stats](Stats.md) (8 shared connections)
- [StatsGenerator](StatsGenerator.md) (1 shared connections)

## Source Files

- `server/models/game.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*