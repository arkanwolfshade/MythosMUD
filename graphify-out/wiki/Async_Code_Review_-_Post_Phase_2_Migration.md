# Async Code Review - Post Phase 2 Migration

> 12 nodes

## Key Concepts

- **.validate_current_vs_max_stats()** (6 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **.max_lucidity()** (4 connections) — `server/models/game.py`
- **.max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **computed_field** (2 connections)
- **Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).…** (2 connections) — `server/models/game.py`
- **Calculate max lucidity based on education. AI: This computed field uses the…** (1 connections) — `server/models/game.py`
- **Calculate max determination points (DP) using formula: (CON + SIZ) / 5. AI:…** (1 connections) — `server/models/game.py`
- **Calculate max lucidity based on education. AI: Helper method to calculate…** (1 connections) — `server/models/game.py`
- **Ensure current_dp (DP), magic_points (MP), and lucidity don't exceed their max…** (1 connections) — `server/models/game.py`

## Relationships

- [server/dependencies.py](server-dependencies.py.md) (6 shared connections)
- [Dark Young of Shub-Niggurath.md](Dark_Young_of_Shub-Niggurath.md.md) (1 shared connections)

## Source Files

- `server/models/game.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*