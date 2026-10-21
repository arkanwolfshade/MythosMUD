# test_build_room_objects_without_environment_in_attributes

> 18 nodes · cohesion 0.25

## Key Concepts

- **test_experience_procedures.py** (9 connections) — `server/tests/integration/test_experience_procedures.py`
- **async_sessionmaker** (7 connections)
- **AsyncSession** (7 connections)
- **test_award_player_xp_is_monotonic_never_decreases_level()** (7 connections) — `server/tests/integration/test_experience_procedures.py`
- **test_level_for_xp_boundaries()** (7 connections) — `server/tests/integration/test_experience_procedures.py`
- **player_row()** (6 connections) — `server/tests/integration/test_experience_procedures.py`
- **asyncio** (6 connections)
- **test_award_player_xp_below_first_level_up_does_not_change_level()** (6 connections) — `server/tests/integration/test_experience_procedures.py`
- **test_award_player_xp_crossing_boundary_levels_up()** (6 connections) — `server/tests/integration/test_experience_procedures.py`
- **test_award_player_xp_rejects_negative_delta()** (6 connections) — `server/tests/integration/test_experience_procedures.py`
- **UUID** (5 connections)
- **test_award_player_xp_unknown_player_returns_no_row()** (5 connections) — `server/tests/integration/test_experience_procedures.py`
- **fixture** (1 connections)
- **parametrize** (1 connections)
- **Integration tests for db/procedures/experience.sql's #879 rewrite:…** (1 connections) — `server/tests/integration/test_experience_procedures.py`
- **Create a user and a player row (level 1, 0 XP, the schema defaults). Yields…** (1 connections) — `server/tests/integration/test_experience_procedures.py`
- **total(L) = 50*L*(L-1): L2=100, L3=300, L10=4500. Boundaries land exactly, not…** (1 connections) — `server/tests/integration/test_experience_procedures.py`
- **A player boosted straight to a high level by one award, then given a tiny…** (1 connections) — `server/tests/integration/test_experience_procedures.py`

## Relationships

- [CombatBroadcastMixin](CombatBroadcastMixin.md) (7 shared connections)

## Source Files

- `server/tests/integration/test_experience_procedures.py`

## Audit Trail

- EXTRACTED: 38 (84%)
- INFERRED: 7 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*