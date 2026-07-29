# Calculate max magic points (MP)

> 11 nodes

## Key Concepts

- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **.max_magic_points()** (3 connections) — `server/models/game.py`
- **.max_lucidity()** (3 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).** (2 connections) — `server/models/game.py`
- **Calculate max lucidity based on education.          AI: This computed field uses** (1 connections) — `server/models/game.py`
- **Calculate max determination points (DP) using formula: (CON + SIZ) / 5.** (1 connections) — `server/models/game.py`
- **Calculate max lucidity based on education.          AI: Helper method to calcula** (1 connections) — `server/models/game.py`
- **Ensure current_dp (DP), magic_points (MP), and lucidity don't exceed their max v** (1 connections) — `server/models/game.py`

## Relationships

- [Core character statistics with Lovecraftian](Core_character_statistics_with_Lovecraftian.md) (6 shared connections)

## Source Files

- `server/models/game.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*