# argon2 auth rationale

> 10 nodes

## Key Concepts

- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **main()** (3 connections) — `scripts/seed_e2e_users.py`
- **E2eUserSpec** (2 connections) — `scripts/seed_e2e_users.py`
- **UUID** (2 connections)
- **datetime** (2 connections)
- **Connection** (1 connections)
- **One row in users plus optional default character for login E2E.** (1 connections) — `scripts/seed_e2e_users.py`
- **Entry point: run E2E user seed via anyio.** (1 connections) — `scripts/seed_e2e_users.py`

## Relationships

- [auth users rationale](auth_users_rationale.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`

## Audit Trail

- EXTRACTED: 28 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*