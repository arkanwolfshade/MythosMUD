# test_players_procedures.py

> 22 nodes

## Key Concepts

- **test_players_procedures.py** (15 connections) — `server/tests/integration/test_players_procedures.py`
- **async_sessionmaker** (10 connections)
- **AsyncSession** (10 connections)
- **asyncio** (9 connections)
- **test_capture_invite_after_reserve_deactivates_and_records_user()** (7 connections) — `server/tests/integration/test_players_procedures.py`
- **test_capture_invite_second_call_returns_false()** (7 connections) — `server/tests/integration/test_players_procedures.py`
- **invite_row()** (6 connections) — `server/tests/integration/test_players_procedures.py`
- **test_capture_invite_unknown_code_returns_false()** (6 connections) — `server/tests/integration/test_players_procedures.py`
- **test_get_user_id_by_username_ci_matches_regardless_of_case()** (6 connections) — `server/tests/integration/test_players_procedures.py`
- **test_reserve_invite_blocks_concurrent_reservation_until_release()** (6 connections) — `server/tests/integration/test_players_procedures.py`
- **user_row()** (6 connections) — `server/tests/integration/test_players_procedures.py`
- **UUID** (6 connections)
- **test_get_user_id_by_username_ci_unknown_username_returns_null()** (5 connections) — `server/tests/integration/test_players_procedures.py`
- **test_reserve_invite_false_for_unknown_code()** (5 connections) — `server/tests/integration/test_players_procedures.py`
- **test_reserve_invite_true_for_active_code()** (5 connections) — `server/tests/integration/test_players_procedures.py`
- **fixture** (2 connections)
- **Integration tests for db/procedures/players.sql's #633/#733 additions:…** (1 connections) — `server/tests/integration/test_players_procedures.py`
- **A caller that captures twice for the same code (skipping a fresh reserve) gets…** (1 connections) — `server/tests/integration/test_players_procedures.py`
- **Two sessions racing reserve_invite() on the same code: the second's…** (1 connections) — `server/tests/integration/test_players_procedures.py`
- **Create one user with a mixed-case username. Yields (user_id, username).** (1 connections) — `server/tests/integration/test_players_procedures.py`
- **Create one active invite. Yields its invite_code.** (1 connections) — `server/tests/integration/test_players_procedures.py`
- **reserve_invite then capture_invite in the same transaction (the real auth-and-…** (1 connections) — `server/tests/integration/test_players_procedures.py`

## Relationships

- [session_factory](session_factory.md) (9 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_players_procedures.py`

## Audit Trail

- EXTRACTED: 55 (86%)
- INFERRED: 9 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*