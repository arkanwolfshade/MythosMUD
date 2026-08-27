# test_profession_service.py

> 15 nodes

## Key Concepts

- **test_players_procedures.py** (10 connections) — `server/tests/integration/test_players_procedures.py`
- **async_sessionmaker** (6 connections)
- **AsyncSession** (6 connections)
- **invite_row()** (5 connections) — `server/tests/integration/test_players_procedures.py`
- **test_get_user_id_by_username_ci_matches_regardless_of_case()** (5 connections) — `server/tests/integration/test_players_procedures.py`
- **test_mark_invite_used_deactivates_and_records_user()** (5 connections) — `server/tests/integration/test_players_procedures.py`
- **test_mark_invite_used_unknown_code_returns_false()** (5 connections) — `server/tests/integration/test_players_procedures.py`
- **user_row()** (5 connections) — `server/tests/integration/test_players_procedures.py`
- **test_get_user_id_by_username_ci_unknown_username_returns_null()** (4 connections) — `server/tests/integration/test_players_procedures.py`
- **asyncio** (4 connections)
- **UUID** (4 connections)
- **fixture** (2 connections)
- **Integration tests for db/procedures/players.sql's #633 additions:…** (1 connections) — `server/tests/integration/test_players_procedures.py`
- **Create one user with a mixed-case username. Yields (user_id, username).** (1 connections) — `server/tests/integration/test_players_procedures.py`
- **Create one active invite. Yields its invite_code.** (1 connections) — `server/tests/integration/test_players_procedures.py`

## Relationships

- [ContainerComponent](ContainerComponent.md) (2 shared connections)

## Source Files

- `server/tests/integration/test_players_procedures.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*