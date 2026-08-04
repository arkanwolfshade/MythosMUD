# argon2 auth rationale

> 12 nodes

## Key Concepts

- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **spawn_defaults.py** (4 connections) — `server/constants/spawn_defaults.py`
- **main()** (3 connections) — `scripts/seed_e2e_users.py`
- **E2eUserSpec** (2 connections) — `scripts/seed_e2e_users.py`
- **UUID** (2 connections)
- **datetime** (2 connections)
- **Connection** (1 connections)
- **One row in users plus optional default character for login E2E.** (1 connections) — `scripts/seed_e2e_users.py`
- **Entry point: run E2E user seed via anyio.** (1 connections) — `scripts/seed_e2e_users.py`
- **Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.** (1 connections) — `server/constants/spawn_defaults.py`

## Relationships

- [npc lifecycle combat](npc_lifecycle_combat.md) (3 shared connections)
- [room models instance](room_models_instance.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/constants/spawn_defaults.py`

## Audit Trail

- EXTRACTED: 33 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*